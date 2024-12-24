from pydantic import BaseModel


class User(BaseModel):
    uid: int
    name: str
    email: str
    password: str
    projects: list[int] = []
    interested_in: list[int] = []
    bio: str = ""

    def __str__(self):
        return self.name



users = [
    User(uid=1, name="Soham", email="soham@gmail.com", password="Hello@123", projects=[101, 102, 104], interested_in=[105, 106], bio="I am a full-stack developer passionate about Python and web technologies."),
    User(uid=2, name="Alex", email="alex@gmail.com", password="Hello@123", projects=[103, 106, 107], interested_in=[108, 109], bio="I enjoy building backends using Java and Flask."),
    User(uid=3, name="Emily", email="emily@gmail.com", password="Hello@123", projects=[104, 110, 112], interested_in=[111, 113], bio="A passionate frontend developer with a focus on React, Angular, and Vue.js."),
]