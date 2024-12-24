from pydantic import BaseModel


class Project(BaseModel):
    uid: int
    name: str
    description: str
    technologies: list[str]


projects = [
    Project(uid=101, name="Project 1", description="Description 1", technologies=["Python", "FastAPI"]),
    Project(uid=102, name="Project 2", description="Description 2", technologies=["JavaScript", "React"]),
    Project(uid=103, name="Project 3", description="Description 3", technologies=["Java", "Spring"]),
    Project(uid=104, name="Project 4", description="Description 4", technologies=["Python", "Django"]),
    Project(uid=105, name="Project 5", description="Description 5", technologies=["JavaScript", "Vue.js"]),
    Project(uid=106, name="Project 6", description="Description 6", technologies=["Python", "Flask"]),
    Project(uid=107, name="Project 7", description="Description 7", technologies=["JavaScript", "Angular"]),
    Project(uid=108, name="Project 8", description="Description 8", technologies=["Java", "Hibernate"]),
    Project(uid=109, name="Project 9", description="Description 9", technologies=["Python", "Pyramid"]),
    Project(uid=110, name="Project 10", description="Description 10", technologies=["JavaScript", "Svelte"]),
    Project(uid=111, name="Project 11", description="Description 11", technologies=["Java", "Spring Boot"]),
    Project(uid=112, name="Project 12", description="Description 12", technologies=["Python", "Django REST Framework"]),
    Project(uid=113, name="Project 13", description="Description 13", technologies=["JavaScript", "Ember.js"]),
    Project(uid=114, name="Project 14", description="Description 14", technologies=["Rust", "Rocket"]),
    Project(uid=115, name="Project 15", description="Description 15", technologies=["JavaScript", "Express.js"]),
    Project(uid=116, name="Project 16", description="Description 16", technologies=[".NET", "ASP.NET Core"]),
    Project(uid=117, name="Project 17", description="Description 17", technologies=["C++", "Qt"]),
    Project(uid=118, name="Project 18", description="Description 18", technologies=["Python", "Dash"]),
    Project(uid=119, name="Project 19", description="Description 19", technologies=["JavaScript", "Backbone.js"]),
    Project(uid=120, name="Project 20", description="Description 20", technologies=["Java", "Play Framework"]),
]