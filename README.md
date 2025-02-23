# Student Management API

This is a **Student Management API** built using **FastAPI**, **N-Tier Architecture**, and 
**Onion Architecture**. The API allows you to manage students by adding new students and 
retrieving their details. The project is containerized using **Docker** and deployed on 
**Kubernetes** with **GitLab CI/CD**.

---

## **Features**
- **Add a new student**: `POST /students`
- **Get all students**: `GET /students`
- **Get a specific student by ID**: `GET /students/{id}`

---

## **Architecture**
The project follows two architectural patterns:
1. **N-Tier Architecture**:
   - **Application Layer**: FastAPI for handling HTTP requests and responses.
   - **Domain Layer**: Contains the core entities (e.g., `Student`).
   - **Core Logic Layer**: Implements business logic (e.g., `StudentService`).
   - **App Handler Layer**: Executes operations and interacts with the API.

2. **Onion Architecture**:
   - **Core Domain**: Contains the `Student` entity and repository interfaces.
   - **Infrastructure Layer**: Implements the repository (e.g., `InMemoryStudentRepository`).
   - **Presentation Layer**: Handles API endpoints and requests.

---

## **Project Structure**
