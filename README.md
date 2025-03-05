
# FastAPI CRUD Application

## Overview

This is a simple FastAPI-based CRUD (Create, Read, Update, Delete) application that provides RESTful API endpoints for managing data. The project is built using FastAPI and uses a database for data persistence.

## Features

- Create new records
- Read existing records
- Update records
- Delete records
- Interactive API documentation with Swagger UI

## Technologies Used

- **FastAPI** - Web framework for building APIs
- **Pydantic** - Data validation and serialization
- **SQLAlchemy** - ORM for database interactions
- **SQLite/PostgreSQL/MySQL** - Database for storing data
- **Uvicorn** - ASGI server for running the application

## Installation

### Prerequisites

Ensure you have Python 3.8+ installed on your system.

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/fastapi-crud-app.git
   cd fastapi-crud-app
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

## API Endpoints

| Method | Endpoint    | Description       |
| ------ | ----------- | ----------------- |
| GET    | /items      | Get all items     |
| GET    | /items/{id} | Get item by ID    |
| POST   | /items      | Create a new item |
| PUT    | /items/{id} | Update an item    |
| DELETE | /items/{id} | Delete an item    |

## Running with Docker (Optional)

1. Build the Docker image:
   ```bash
   docker build -t fastapi-crud .
   ```
2. Run the container:
   ```bash
   docker run -p 8000:8000 fastapi-crud
   ```

## API Documentation

Once the app is running, you can access API documentation:

- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)



