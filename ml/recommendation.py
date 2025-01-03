import pinecone
from sentence_transformers import SentenceTransformer
import pandas as pd
from datetime import datetime as dt

class VectorRecommender:
    def __init__(self, api_key, environment):
        # Initialize Pinecone
        pinecone.init(api_key=api_key, environment=environment)
        
        # Initialize SBERT model
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        
        # Create or get index
        self.index_name = "project-embeddings"
        if self.index_name not in pinecone.list_indexes():
            pinecone.create_index(
                self.index_name,
                dimension=384,  # all-MiniLM-L6-v2 dimension
                metric="cosine"
            )
        self.index = pinecone.Index(self.index_name)

    def create_project_embedding(self, project_data):
        # Combine project features into a single text
        text = f"{project_data['name']} {project_data['description']} {project_data['languages']}"
        # Create embedding
        return self.model.encode(text).tolist()

    def store_project(self, project_id, project_data):
        # Create embedding for project
        vector = self.create_project_embedding(project_data)
        
        # Store in Pinecone
        self.index.upsert(
            vectors=[(str(project_id), vector)],
            metadata={"timestamp": str(dt.now())}
        )

    def get_similar_projects(self, project_id, k=5):
        # Get project vector
        vector = self.index.fetch([str(project_id)])
        
        # Query similar vectors
        results = self.index.query(
            vector=vector[str(project_id)]['vector'],
            top_k=k,
            include_metadata=True
        )
        
        return [int(match['id']) for match in results['matches']]