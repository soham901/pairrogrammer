from sqlmodel import SQLModel, Field, JSON


class Project(SQLModel, table=True):
    pid: int = Field(default=None, primary_key=True)
    name: str
    description: str
    tags: str
