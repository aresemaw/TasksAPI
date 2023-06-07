# Task API

Task API is a simple Flask application that provides an API for managing tasks. It allows users to perform CRUD (Create, Read, Update, Delete) operations on tasks.

## Prerequisites

Before running the application, make sure you have the following installed:

- Python 3.x
- Flask
- Flask-RESTful
- Flask-SQLAlchemy

## Installation

1. Clone the repository and navigate to the project directory:
$ git clone https://github.com/your-username/task-api.git
$ cd task-api

2. Create and activate a virtual environment (optional but recommended):
$ python3 -m venv venv
$ source venv/bin/activate

3. Install the required dependencies:
$ pip install -r requirements.txt

4. Create the SQLite database file:
$ python
>>> from app import db
>>> db.create_all()
>>> exit()

## Usage

1. Start the Flask development server:
$ python app.py

2. Open your web browser and go to http://localhost:5000 to access the Task API homepage.

3. Features:
- Use the "Get Tasks" button to retrieve all tasks.
- Use the "Add Task" button to add a new task.
- Use the "Update Task" button to update an existing task.
- Use the "Delete Task" button to delete a task.

4. API Endpoints:
- GET /tasks - Get all tasks
- GET /tasks/{task_id} - Get a specific task
- POST /tasks - Add a new task
- PUT /tasks/{task_id} - Update a task
- DELETE /tasks/{task_id} - Delete a task
