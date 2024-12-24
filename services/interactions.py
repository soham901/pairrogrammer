from sqlmodel import select

from ..models.projects import Project
from ..models.interactions import Interaction


class InteractionService:
    def __init__(self, session):
        self.session = session

    def get_interactions(self, user_id: int):
        # Perform a join between Interaction and Project tables
        statement = select(Interaction, Project).join(
            Project, Project.pid == Interaction.item_id
        ).where(Interaction.user_id == user_id)

        # Execute the statement and return the results
        results = self.session.exec(statement)
        return results.all()
        

    
    def add_interaction(self, interaction: Interaction):
        self.session.add(interaction)
        self.session.commit()
        self.session.refresh(interaction)
        return interaction