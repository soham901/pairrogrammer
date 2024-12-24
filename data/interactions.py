from pydantic import BaseModel
import pandas as pd

class Interaction(BaseModel):
    user_id: int
    item_id: int
    rating: float

interactions_data = [
    Interaction(user_id=1, item_id=101, rating=1),
    Interaction(user_id=1, item_id=102, rating=1),
    Interaction(user_id=2, item_id=101, rating=1),
    Interaction(user_id=2, item_id=102, rating=1),
    Interaction(user_id=2, item_id=103, rating=1),
    Interaction(user_id=3, item_id=101, rating=1),
    Interaction(user_id=3, item_id=102, rating=1),
    Interaction(user_id=3, item_id=104, rating=1),
    Interaction(user_id=3, item_id=105, rating=1),
    Interaction(user_id=4, item_id=106, rating=1),
    Interaction(user_id=4, item_id=107, rating=1),
]


interactions_dict = [interaction.dict() for interaction in interactions_data]

interactions = pd.DataFrame(interactions_dict)

# interactions = pd.read_csv('interactions_100089.csv')
