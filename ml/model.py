from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split
from surprise import accuracy
import pandas as pd
from datetime import datetime as dt
from recommendation import VectorRecommender

class HybridRecommender:
    def __init__(self, pinecone_api_key, pinecone_env):
        # Initialize both recommenders
        self.cf_model = SVD()
        self.vector_recommender = VectorRecommender(
            api_key=pinecone_api_key,
            environment=pinecone_env
        )
        self.is_trained = False

    def train_collaborative_model(self, interactions_file):
        interactions = pd.read_csv(interactions_file)
        reader = Reader(rating_scale=(0, 1))
        data = Dataset.load_from_df(
            interactions[['user_id', 'item_id', 'rating']], 
            reader
        )
        
        trainset, testset = train_test_split(data, test_size=0.2)
        self.cf_model.fit(trainset)
        self.is_trained = True
        
        # Evaluate
        predictions = self.cf_model.test(testset)
        rmse = accuracy.rmse(predictions)
        print(f"RMSE: {rmse}")

    def store_project(self, project_id, project_data):
        self.vector_recommender.store_project(project_id, project_data)

    def get_recommendations(self, user_id, project_id=None, n=10):
        recommendations = set()
        
        # Get collaborative filtering recommendations
        if self.is_trained:
            cf_recs = self._get_cf_recommendations(user_id, n)
            recommendations.update(cf_recs)
        
        # Get vector-based recommendations
        if project_id:
            vector_recs = self.vector_recommender.get_similar_projects(project_id, k=n)
            recommendations.update(vector_recs)
        
        return list(recommendations)[:n]

    def _get_cf_recommendations(self, user_id, n):
        # Get all items
        all_items = self._get_all_items()
        
        # Predict ratings for all items
        predictions = []
        for item_id in all_items:
            pred = self.cf_model.predict(user_id, item_id)
            predictions.append((item_id, pred.est))
        
        # Sort and return top N
        predictions.sort(key=lambda x: x[1], reverse=True)
        return [p[0] for p in predictions[:n]]

    def _get_all_items(self):
        # Implement this based on your data storage
        pass


# from surprise import Dataset, Reader, SVD
# from surprise.model_selection import train_test_split
# import pandas as pd
# from datetime import datetime as dt

# interactions = pd.read_csv("interactions.csv")

# # Load the data into Surprise's Dataset
# reader = Reader(rating_scale=(0, 1))
# data = Dataset.load_from_df(interactions[['user_id', 'item_id', 'rating']], reader)
# num_of_records = len(interactions)

# # Train-test split (optional but good practice)
# trainset, testset = train_test_split(data, test_size=0.2)

# # Collaborative Filtering model (SVD)
# model = SVD()

# print(f"\nTraining the model... with {num_of_records}\n")
# start_time = dt.now()

# # Fit the model with the training set
# model.fit(trainset)

# # Optionally, make predictions on the test set (for evaluation)
# predictions = model.test(testset)

# # Optionally, evaluate RMSE (Root Mean Squared Error)
# from surprise import accuracy
# rmse = accuracy.rmse(predictions)
# print(f"RMSE: {rmse}")
# print(f"\nModel training completed in {(dt.now() - start_time).total_seconds()} seconds.\n")
