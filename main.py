from fastapi import FastAPI
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split
import pandas as pd

app = FastAPI()

data_path = "interactions.csv"
interactions = pd.read_csv(data_path)

reader = Reader(rating_scale=(0, 1))
data = Dataset.load_from_df(interactions[['user_id', 'item_id', 'rating']], reader)

# Collaborative Filtering model
trainset = data.build_full_trainset()
model = SVD()
model.fit(trainset)

@app.get("/")
def home():
    return {"message": "Welcome to the Pairrogrammer API"}

@app.get("/recommend/{user_id}")
def recommend(user_id: int, n: int = 5):
    """
    Recommend `n` items to the given user.
    """
    all_items = interactions['item_id'].unique()

    known_items = interactions[interactions['user_id'] == user_id]['item_id'].tolist()

    recommendations = []
    
    for item in all_items:
        if item not in known_items:
            predicted_rating = model.predict(user_id, item).est
            recommendations.append((int(item), float(predicted_rating)))

    recommendations.sort(key=lambda x: x[1], reverse=True)

    return {"user_id": user_id, "recommendations": recommendations[:n]}
