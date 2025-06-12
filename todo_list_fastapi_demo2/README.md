# FastAPI To-Do List Manager

A simple in-memory To-Do list manager built with FastAPI.

## Features

- Get all to-do items
- Create new to-do items
- Delete to-do items by ID

## Installation

```bash
# Clone the repository
git clone <repository-url>
cd <repository-directory>

# Install dependencies
pip install -r requirements.txt
```

## Running the Application

```bash
uvicorn app.main:app --reload
```

The API will be available at http://localhost:8000

## API Documentation

Once the application is running, you can access the interactive API documentation at:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API Endpoints

### GET /todos

Returns a list of all to-do items.

Example response:
```json
[
  {
    "id": 1,
    "task": "Learn FastAPI"
  }
]
```

### POST /todos

Creates a new to-do item.

Request body:
```json
{
  "task": "Build an amazing app"
}
```

Example response:
```json
{
  "id": 2,
  "task": "Build an amazing app"
}
```

### DELETE /todos/{item_id}

Deletes a to-do item by ID.

Example response:
```json
{
  "status": "success",
  "message": "To-Do item with id 2 deleted"
}
```
