# Fitness App

A full-stack fitness and endurance-training platform designed to help athletes track workouts, analyze performance, and connect with other athletes. This started because while triathlon training I wanted to track customized metrics which were not available out of the box in other workout tracking apps.

The project focuses on building a scalable backend and processing detailed workout data. I've wanted to gain experience developing with Vue.js so as the project grows I've continued to add new features to the frontend. This idea extends to other integrations as well.

## Key Features

- **Workout Tracking & Analytics:** Record workouts and analyze historical training data, including heart rate, speed, cadence, power, elevation, and GPS coordinates.
- **Workout Data Visualization:** Explore workout routes, performance metrics, and historical activity data through interactive maps and visualizations.
- **FIT File Import:** Import structured workout data from FIT files to populate workout records and associated performance metrics.
- **Social Features:** Follow other athletes, interact with workouts through likes and comments, and build a connected fitness community.
- **Messaging & Notifications:** In-app messaging and notifications to keep users informed about social activity and application events.
- **Asynchronous Processing:** Background task processing for email notifications and other application workflows using Celery and Redis.
- **User Profiles:** Manage user accounts, personal information, and workout history.

## Technology Stack

| Category              | Technologies                                     |
| --------------------- | ------------------------------------------------ |
| Backend               | Python, Django, Django REST Framework            |
| Frontend              | Vue 3, TypeScript                                |
| State Management      | Pinia                                            |
| Database              | PostgreSQL                                       |
| Background Processing | Celery, Redis                                    |
| API Communication     | REST API, Axios                                  |
| Mapping               | Leaflet                                          |
| Development & Quality | Poetry, pytest, pre-commit, Flake8, Black, isort |

## Architecture

The application follows a decoupled frontend/backend architecture.

- **Backend:** Django REST Framework provides RESTful API endpoints for user management, workout tracking, social interactions, and application functionality.
- **Frontend:** Vue 3 and TypeScript provide a responsive, component-based interface with Pinia managing application state.
- **Database:** PostgreSQL stores user information, workout records, performance samples, and social interactions.
- **Background Workers:** Celery processes asynchronous tasks using Redis as its message broker, allowing time-consuming operations and notifications to execute independently of API requests.

## Development Goals

This project is an ongoing effort to build a comprehensive endurance-training platform while exploring full-stack software engineering concepts, including:

- Designing and implementing RESTful APIs.
- Building scalable relational database models and query workflows.
- Processing and analyzing time-series workout data.
- Implementing asynchronous task processing and event-driven workflows.
- Developing interactive data visualizations and mapping functionality.
- Integrating external fitness data sources and wearable devices.
- Implementing automated testing, linting, and code quality workflows.

## Future Enhancements

- Garmin integration for automated workout synchronization.
- Advanced training analytics and performance trends.
- Heart rate zone analysis and training load metrics.
- Expanded nutrition and recovery tracking.
- Additional social and community features.
