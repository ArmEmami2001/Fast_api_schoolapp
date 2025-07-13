FastAPI School Management API
A simple, modern, and fast API for a basic school management system built with FastAPI, SQLAlchemy, and SQLite. This project demonstrates core concepts of building RESTful APIs in Python, including CRUD operations, dependency injection, and data validation with Pydantic.
Features
Student Management: Create, Read, Update, and Delete (CRUD) student records.
Course Management: Create courses and assign them to specific students.
Interactive API Docs: Automatic, interactive API documentation powered by Swagger UI and ReDoc.
Data Validation: Robust request and response data validation using Pydantic schemas.
Relational Database: Uses SQLAlchemy ORM to interact with a SQLite database.
Technologies Used
Python 3.7+
FastAPI: The modern web framework for building APIs.
Uvicorn: The lightning-fast ASGI server to run the application.
SQLAlchemy: The Python SQL toolkit and Object Relational Mapper.
Pydantic: For data validation and settings management.
SQLite: The lightweight, file-based SQL database engine.
Project Structure
.
├── main.py         # Main application file with API endpoints
├── models.py       # SQLAlchemy database models
├── schemas.py      # Pydantic data schemas for validation
└── database.py     # Database connection and session setup
└── school.db       # The SQLite database file (created on run)



Setup and Installation
Follow these steps to get the project up and running on your local machine.
1. Clone the Repository
First, clone this repository to your local machine (or simply create the files as described above).
git clone <your-repository-url>
cd <your-project-directory>



2. Create and Activate a Virtual Environment
It is highly recommended to use a virtual environment to manage project dependencies.
# Create the virtual environment
python -m venv venv

# Activate it (on Windows)
venv\Scripts\activate

# Activate it (on macOS/Linux)
source venv/bin/activate



3. Install Dependencies
Install all the required packages using pip.
pip install fastapi "uvicorn[standard]" sqlalchemy



Running the Application
Once the setup is complete, you can run the application using Uvicorn.
uvicorn main:app --reload



The server will start on http://127.0.0.1:8000.
The --reload flag enables live reloading, which automatically restarts the server when you make changes to the code.
How to Use
The API is fully documented and interactive. Once the server is running, navigate to http://127.0.0.1:8000/docs in your browser.
This will open the Swagger UI, where you can see all the available endpoints, their expected inputs, and test them live.
API Endpoints
| Method | Path | Description |
| POST | /students/ | Create a new student. |
| GET | /students/ | Get a list of all students. |
| GET | /students/{student_id} | Get a specific student by their ID. |
| PUT | /students/{student_id} | Update a student's information. |
| DELETE | /students/{student_id} | Delete a student by their ID. |
| POST | /students/{student_id}/courses/ | Create a new course for a student. |
| GET | /courses/ | Get a list of all courses. |
