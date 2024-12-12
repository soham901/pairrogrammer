# Project Plan for Pairrogrammer

## Core Idea

A mobile app where CS students and project builders can connect to find their ideal collaborators based on skills, project ideas, and mutual interests. The platform integrates AI-driven recommendations, intuitive UI, and gamification to create an engaging user experience.

## Roles and Responsibilities

### 1. Model Monk (Friend 1)

#### Responsibilities:

- AI-Driven Matching System:

  - Develop and fine-tune matching algorithms using user inputs such as skills, interests, experience, and project history.
  - Use pre-trained LLMs (e.g., Ollama, Hugging Face) for enhanced recommendations.

- Skill Recommendation AI:

  - Suggest learning resources and personalized skill improvement paths.

- NLP for Project Tagging:

  - Auto-tag project descriptions with relevant categories using NLP.

- Backend Integration:
  - Expose AI functionalities via FastAPI endpoints for use by the backend.

#### Tools:

- Python (FastAPI, scikit-learn, or TensorFlow/PyTorch).
- Ollama or Hugging Face for LLMs.
- Postgres for storing training data and user stats.

### 2. Pixel Pirate (Friend 2)

#### Responsibilities:

- UI/UX Design:

  - Create an interactive and fun UI with swipe-based match interactions and engaging animations.

- Gamification:

  - Design badges, streaks, points, and leaderboards to enhance user engagement.

- User Flows:

  - Smooth onboarding, seamless matching, and intuitive collaboration management.

- Responsive Design:
  - Ensure the app is highly responsive on mobile devices.

#### Tools:

- Figma or Adobe XD for prototypes.
- Flutter for building the mobile app.
- Lottie for animations.

### 3. Stack Sultan (Me)

#### Responsibilities:

- Backend Development:
  - Implement APIs with Hono (TypeScript) for:
    - User authentication (GitHub, email).
    - Matchmaking and project data handling.
    - Handling project CRUD (Create, Read, Update, Delete).
  - Integrate FastAPI AI endpoints for real-time recommendations.
- Frontend Integration:
  - Ensure smooth communication between Flutter app and backend APIs.
- Database Management:
  - Design Postgres schema for users, projects, and matches.
  - Optimize queries for performance and scalability.
- DevOps:
  - Set up deployment pipelines, containerization (Docker), and scalable hosting solutions.
  - Use GitHub Actions for CI/CD.

#### Tools:

- Hono (TypeScript) for backend.
- Flutter for mobile development.
- Postgres for database.
- Docker for containerization.
- GitHub Actions for CI/CD.

# Feature Development Timeline

## Week 1: Planning and Setup

### Define MVP features:

- User authentication. 🔧
- Skill-based matchmaking. 🔧
- Project creation and collaboration. 🤝

### Set up the development environment:

- Backend (Hono + FastAPI). 🤝
- Flutter app. 🤝
- Postgres database. 🤝

### Design database schema:

- Users: id, name, email, skills, interests, badges. 🔧
- Projects: id, title, description, skills_required, collaborators. 🔧
- Matches: id, user_id, match_id, compatibility_score. 🔧

### Research and implement mock ML models:

- Skill recommendation, project tagging, and matchmaking. 🤝

### Create basic user flows in Flutter:

- Onboarding. 🤝
- Project creation. 🤝
- Project collaboration. 🤝

## Week 2: Backend and ML Development

### Build Hono APIs for:

- User authentication and profile management. 🔧
- Fetching and updating project data. 🔧
- Fetching match recommendations from ML models. 🤝

### Develop the ML recommendation system:

- Train/test matching algorithm on dummy data. 🔧
- Create APIs in FastAPI to expose ML model results. 🤝

## Week 3: Mobile App UI Development

### Design key screens in Flutter:

- Home: Skill-based matches (Tinder-style swipe interface). 🤝
- Profile: Show skills, badges, and projects. 🤝
- Projects: Manage created and joined projects. 🤝

### Integrate backend APIs:

- Fetch user profiles, matches, and projects. 🤝

## Week 4: Gamification and Final Touches

### Add gamified features:

- Points and badges for completing projects or contributing skills. 🤝
- Leaderboard for top collaborators. 🤝

### Optimize ML model recommendations based on user feedback: 🤝

### Test the app:

- Debug API integrations and UI flows. 🤝
- Run performance tests on ML endpoints. 🔧

## Future Features (Post-MVP)

### Chat Integration:

- Allow users to communicate within the app. 🤝
- Use WebSockets for real-time messaging. 🤝

### AI-Powered Project Creation:

- Generate project ideas using third party models (via Ollama or Hugging Face). 🤝

### Cross-Platform Expansion:

- Build a web version of the app for desktops (using Flutter Web or React). 🔧

### Skill Assessment:

- Include quizzes or coding challenges to verify users' skills. 🤝

### Social Sharing:

- Let users share project updates or achievements on social media. 🤝
