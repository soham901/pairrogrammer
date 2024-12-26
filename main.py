from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from sqlmodel import create_engine, SQLModel, Session
from fastapi.middleware.cors import CORSMiddleware

from .services.interactions import InteractionService, Interaction
from .services.projects import ProjectService, Project

app = FastAPI(
    title="Pairrogrammer API",
    description="API for Pairrogrammer",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["POST", "GET", "PATCH", "PUT", "DELETE"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    # return {"message": "Welcome to the Pairrogrammer API"}
    with open("index.html") as f:
        html_content = f.read()
        return HTMLResponse(content=html_content, status_code=200)
    return {"message": "Welcome to the Pairrogrammer API"}


@app.get("/interactions/{user_id}")
def get_interactions(user_id: int):
    with Session(engine) as session:
        interaction_service = InteractionService(session)
        return interaction_service.get_interactions(user_id)
    

@app.post("/interactions")
def add_interaction(interaction: Interaction):
    with Session(engine) as session:
        interaction_service = InteractionService(session)
        return interaction_service.add_interaction(interaction)

@app.get("/projects")
def get_projects(user_id: int):
    with Session(engine) as session:
        project_service = ProjectService(session)
        return project_service.get_projects(user_id=user_id)


@app.get("/projects/{project_id}")
def get_project(project_id: int):
    with Session(engine) as session:
        project_service = ProjectService(session)
        return project_service.get_project(project_id)


@app.post("/projects")
def add_project(project: Project):
    with Session(engine) as session:
        project_service = ProjectService(session)
        return project_service.add_project(project)


# take the left or right swipe and add the interaction
@app.post("/projects/{project_id}/swipe")
def swipe_project(project_id: int, user_id: int, swipe: str):
    with Session(engine) as session:
        project_service = ProjectService(session)
        return project_service.swipe_project(project_id, user_id, swipe)


# list out the right swiped projects
@app.get("/intrested-projects/{user_id}")
def get_matches(user_id: int):
    with Session(engine) as session:
        project_service = ProjectService(session)
        return project_service.get_matches(user_id)



# @app.get("/projects/{project_id}")
# def get_project(project_id: int):
#     project = next((project for project in projects if project["id"] == project_id), None)
#     if project is None:
#         raise HTTPException(status_code=404, detail="Project not found")
#     return project


# @app.get("/users")
# def get_users():
#     return users


# @app.get("/users/{user_id}")
# def get_user(user_id: int):
#     user = next((user for user in users if user["id"] == user_id), None)
#     if user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user


# @app.get("/interactions/{user_id}")
# def get_interactions(user_id: int):
#     return interactions[interactions["user_id"] == user_id].to_dict(orient="records")

# @app.get("/recommend/{user_id}")
# def recommend(user_id: int, n: int = 5) -> dict:
#     """
#     Recommend `n` items to the given user.
#     """
#     unique_users = interactions['user_id'].unique()
#     unique_items = interactions['item_id'].unique()

#     if user_id not in unique_users:
#         return {"error": f"User {user_id} not found in the dataset."}
    
#     known_items = interactions[interactions['user_id'] == user_id]['item_id'].tolist()

#     recommendations = []
    
#     # Loop through all items (projects) and calculate the predicted ratings for those the user has not yet interacted with
#     for item in unique_items:
#         if item not in known_items:
#             predicted_rating = model.predict(user_id, item).est
#             # Get the project details by matching the project ID with the item
#             project = next((project for project in projects if project.uid == item), None)
#             if project:
#                 print(project)
#                 recommendations.append({
#                     "project_id": item,
#                     "predicted_rating": float(predicted_rating),
#                     "project_details": project
#                 })

#     # Sort recommendations by predicted rating in descending order
#     recommendations.sort(key=lambda x: x["predicted_rating"], reverse=True)

#     return {
#         "user_id": user_id,
#         "recommendations": [rec["project_details"] for rec in recommendations[:n]]
#     }


# # add interaction route (POST) with user_id, item_id, rating
# @app.post("/interactions")
# def add_interaction(user_id: int, item_id: int, rating: int):
#     interactions_data.append({"user_id": user_id, "item_id": item_id, "rating": rating})
#     return {"message": "Interaction added successfully."}


engine = create_engine("sqlite:///database.db")

SQLModel.metadata.create_all(engine)