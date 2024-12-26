from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split
import pandas as pd
from datetime import datetime as dt

interactions = pd.read_csv("interactions.csv")

# Load the data into Surprise's Dataset
reader = Reader(rating_scale=(0, 1))
data = Dataset.load_from_df(interactions[['user_id', 'item_id', 'rating']], reader)
num_of_records = len(interactions)

# Train-test split (optional but good practice)
trainset, testset = train_test_split(data, test_size=0.2)

# Collaborative Filtering model (SVD)
model = SVD()

print(f"\nTraining the model... with {num_of_records}\n")
start_time = dt.now()

# Fit the model with the training set
model.fit(trainset)

# Optionally, make predictions on the test set (for evaluation)
predictions = model.test(testset)

# Optionally, evaluate RMSE (Root Mean Squared Error)
from surprise import accuracy
rmse = accuracy.rmse(predictions)
print(f"RMSE: {rmse}")
print(f"\nModel training completed in {(dt.now() - start_time).total_seconds()} seconds.\n")
