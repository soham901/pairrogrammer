from fastapi import FastAPI, HTTPException

from .data.projects import projects
from .data.users import users
from .data.interactions import interactions_data
from .ml.model import model, interactions

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Pairrogrammer API"}


@app.get("/projects")
def get_projects():
    return projects


@app.get("/projects/{project_id}")
def get_project(project_id: int):
    project = next((project for project in projects if project["id"] == project_id), None)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return project


@app.get("/users")
def get_users():
    return users


@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = next((user for user in users if user["id"] == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.get("/interactions/{user_id}")
def get_interactions(user_id: int):
    return interactions[interactions["user_id"] == user_id].to_dict(orient="records")

@app.get("/recommend/{user_id}")
def recommend(user_id: int, n: int = 5) -> dict:
    """
    Recommend `n` items to the given user.
    """
    unique_users = interactions['user_id'].unique()
    unique_items = interactions['item_id'].unique()

    if user_id not in unique_users:
        return {"error": f"User {user_id} not found in the dataset."}
    
    known_items = interactions[interactions['user_id'] == user_id]['item_id'].tolist()

    recommendations = []
    
    # Loop through all items (projects) and calculate the predicted ratings for those the user has not yet interacted with
    for item in unique_items:
        if item not in known_items:
            predicted_rating = model.predict(user_id, item).est
            # Get the project details by matching the project ID with the item
            project = next((project for project in projects if project.uid == item), None)
            if project:
                print(project)
                recommendations.append({
                    "project_id": item,
                    "predicted_rating": float(predicted_rating),
                    "project_details": project
                })

    # Sort recommendations by predicted rating in descending order
    recommendations.sort(key=lambda x: x["predicted_rating"], reverse=True)

    return {
        "user_id": user_id,
        "recommendations": [rec["project_details"] for rec in recommendations[:n]]
    }


# add interaction route (POST) with user_id, item_id, rating
@app.post("/interactions")
def add_interaction(user_id: int, item_id: int, rating: int):
    interactions_data.append({"user_id": user_id, "item_id": item_id, "rating": rating})
    return {"message": "Interaction added successfully."}