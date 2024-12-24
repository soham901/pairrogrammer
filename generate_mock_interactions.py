import pandas as pd
import random

# Define the structure of the CSV
columns = ["user_id", "item_id", "rating"]
data = []

# Generate synthetic data
num_users = int(input("Enter the number of users: "))
num_items = int(input("Enter the number of items: "))
ratings = [0, 1]  # Binary ratings (0 = dislike, 1 = like)

# Populate the data
for user_id in range(1, num_users + 1):
    for _ in range(random.randint(5, 15)):  # Each user interacts with 5-15 items
        item_id = random.randint(1, num_items)
        rating = random.choice(ratings)
        data.append([user_id, item_id, rating])

# Create a DataFrame
df = pd.DataFrame(data, columns=columns)

num_of_records = len(df)

# Save to CSV
output_path = f"interactions_{num_of_records}.csv"
df.to_csv(output_path, index=False)
