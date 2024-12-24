from sqlmodel import SQLModel, Field
from sqlalchemy import UniqueConstraint


class Interaction(SQLModel, table=True):
    __table_args__ = (
        UniqueConstraint('user_id', 'pro_id', name='unique_user_project'),
    )
    
    id: int = Field(default=None, primary_key=True)
    user_id: int
    pro_id: int | None = Field(default=None, foreign_key="project.pid")
    is_interested: bool