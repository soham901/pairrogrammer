from sqlmodel import select, and_

from ..models.projects import Project
from ..models.interactions import Interaction


class ProjectService:
    def __init__(self, session):
        self.session = session

    def get_projects(self, user_id: int):
        # Select projects that the user has not swiped
        statement = (
            select(Project)
            .join(Interaction, and_(Project.pid == Interaction.pro_id, Interaction.user_id == user_id), isouter=True)
            .where(Interaction.id.is_(None))
        )
        projects = self.session.exec(statement).all()
        return projects
    

    def get_projects_by_id(self, project_id: int):
        project = self.session.exec(select(Project).where(Project.pid == project_id)).first()
        return project
    
    def get_projects_of_user(self, user_id: int):
        projects = self.session.exec(select(Project).where(Project.user_id == user_id)).all()
        return projects
    
    def add_project(self, project: Project):
        self.session.add(project)
        self.session.commit()
        self.session.refresh(project)
        return project

    def swipe_project(self, project_id: int, user_id: int, swipe: str):
        project = self.get_projects_by_id(project_id)
        if project is None:
            return None
        
        interaction = Interaction(
            pro_id=project_id,
            user_id=user_id,
            is_interested=swipe == "right"
        )

        self.session.add(interaction)
        self.session.commit()
        self.session.refresh(interaction)
        return interaction

    def get_matches(self, user_id: int):
        statement = (
            select(Project)
            .join(Interaction, and_(Project.pid == Interaction.pro_id, Interaction.user_id == user_id))
            .where(Interaction.is_interested == True)
        )
        projects = self.session.exec(statement).all()
        return projects

    def seed(self):
        # if data already exists, do not seed
        projects = self.session.exec(select(Project)).all()
        if projects:
            return
        
        projects = [
            Project(user_id=1, name="CLI Project", description="CLI tool to manage files", tags="java,cli"),
            Project(user_id=1, name="Todo App", description="A simple todo app", tags="html,css,js"),
            Project(user_id=2, name="Django Project", description="A web app using Django", tags="python,django"),
            Project(user_id=2, name="Flask Project", description="A web app using Flask", tags="python,flask"),
            Project(user_id=3, name="React Project", description="A web app using React", tags="javascript,react"),
            Project(user_id=3, name="Vue Project", description="A web app using Vue", tags="javascript,vue"),
            Project(user_id=4, name="Angular Project", description="A web app using Angular", tags="javascript,angular"),
            Project(user_id=4, name="Svelte Project", description="A web app using Svelte", tags="javascript,svelte"),
            Project(user_id=5, name="Express Project", description="A web app using Express", tags="javascript,express"),
            Project(user_id=5, name="Nest Project", description="A web app using Nest", tags="javascript,nest"),
            Project(user_id=6, name="Spring Project", description="A web app using Spring", tags="java,spring"),
            Project(user_id=6, name="JDBC Project", description="A web app using JDBC", tags="java,jdbc"),
        ]
        self.session.add_all(projects)
        self.session.commit()