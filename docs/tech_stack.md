# Tech Stack for Pairrogrammer

Pairrogrammer is built with a modern, efficient, and scalable tech stack to ensure smooth functionality and a seamless user experience. Here’s an overview of the core technologies used in the project:

## 1. **Mobile App**: Flutter 📱

- **Flutter**: The app is developed using Flutter to ensure a smooth, cross-platform user experience. Flutter allows us to build natively compiled applications for mobile (iOS and Android) from a single codebase.
- **Dart**: Flutter uses Dart as its programming language, enabling fast development and high-performance apps.

### Why Flutter?

- **Cross-Platform**: One codebase for both iOS and Android.
- **Rich UI**: Offers a rich set of pre-designed widgets, allowing us to create engaging and beautiful UI/UX.
- **Fast Development**: Hot-reload feature for rapid development.

## 2. **Backend**: Hono + FastAPI ⚙️

- **Hono**: A lightweight, fast, and secure web framework for building APIs with TypeScript. It is used to build the main backend APIs for Pairrogrammer, including authentication, project management, and matchmaking.
- **FastAPI**: Used for handling the AI-powered matchmaking system and providing the backend services for model inference. FastAPI allows for quick and easy creation of APIs and integrates well with Python-based AI models.

### Why Hono + FastAPI?

- **Performance**: Both Hono and FastAPI are known for their high performance, handling high loads and providing fast response times.
- **Ease of Use**: FastAPI simplifies working with Python-based models, and Hono is perfect for TypeScript developers.
- **Scalability**: Both frameworks are highly scalable and can handle growing user bases.

## 3. **Database**: PostgreSQL 🗃️

- **PostgreSQL**: A powerful, open-source relational database system that stores data for Pairrogrammer, including user profiles, project data, and match information.

### Why PostgreSQL?

- **Reliability**: PostgreSQL is a mature and stable database known for its reliability and data integrity.
- **Advanced Features**: It supports advanced SQL features such as indexing, full-text search, and complex queries.
- **Scalability**: PostgreSQL can handle large datasets and is scalable for high traffic applications.

## 4. **AI Models**: FastAPI + Ollama 🤖

- **FastAPI for AI**: FastAPI exposes the AI models to the backend via APIs. It handles the inference requests and returns AI-powered recommendations for matchmaking, skill suggestions, and project categorization.
- **Ollama**: For leveraging pre-trained language models (LLMs) like GPT-based models for generating project ideas, assisting with skills recommendations, and enhancing overall AI functionality.

### Why FastAPI + Ollama?

- **Speed**: FastAPI is optimized for AI services, allowing quick inference and seamless integration of models.
- **AI Customization**: Ollama allows easy integration with LLMs and other AI services to create intelligent features for matching and project suggestions.

## 5. **Containerization & Deployment**: Docker + CI/CD 🐳

- **Docker**: Used to containerize the backend and AI services for easy deployment and scaling. Docker ensures the app runs consistently across different environments.
- **CI/CD with GitHub Actions**: GitHub Actions automates the build, test, and deployment process, ensuring smooth continuous integration and delivery.

### Why Docker & CI/CD?

- **Portability**: Docker ensures that the application works on any machine, from local development environments to production servers.
- **Automation**: CI/CD pipelines automate testing and deployment, reducing manual work and improving reliability.

## 6. **Hosting & Deployment**: Fly.io, Render 🌐

- **Fly.io**: Used for deploying the backend and AI services to a scalable cloud infrastructure.
- **Render**: Used for hosting the Flutter app’s backend services.

### Why Fly.io & Render?

- **Scalability**: Fly.io offers seamless scaling for global applications.
- **Ease of Use**: Render allows for easy deployment with automatic SSL certificates and simplified configuration.

## 7. **Version Control**: Git + GitHub 🧑‍💻

- **Git**: Git is used for version control, ensuring that all team members are on the same page when developing features and fixing bugs.
- **GitHub**: All code is hosted on GitHub, providing collaboration tools like pull requests, issue tracking, and CI/CD integration.

### Why Git + GitHub?

- **Collaboration**: GitHub provides an easy way for team members to collaborate and review each other's code.
- **Version Control**: Git tracks changes to the codebase, enabling easy rollbacks and version management.

---

## Conclusion

Pairrogrammer combines a modern tech stack with AI-powered recommendations and cross-platform support to provide a user-friendly and scalable platform for CS students and project builders. The combination of **Flutter**, **Hono**, **FastAPI**, **PostgreSQL**, **Ollama**, and **Docker** ensures that the app is fast, reliable, and future-proof.

## Breakdown:

- Mobile App: Uses Flutter for its cross-platform capability, ensuring a responsive experience on both iOS and Android.
- Backend: Uses Hono for API handling and FastAPI for AI integrations.
- Database: Uses PostgreSQL for structured data storage and management.
- AI Models: FastAPI and Ollama power the AI features like matchmaking and project idea generation.
- Containerization: Docker enables smooth deployment, while GitHub Actions handles CI/CD.
- Hosting: Services are deployed on Fly.io and Render for scalability and performance.
