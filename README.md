# Student-Management-System

A super fast REST API to manage student records. Built with **FastAPI** and includes a built-in **Admin Dashboard** to manage the database easily.

## The Stack

* **Framework:** FastAPI
* **Database:** SQLite (via SQLAlchemy)
* **Admin Panel:** SQLAdmin
* **Validation:** Pydantic

## How to Run

1.  **Install dependencies**
    ```bash
    pip install fastapi uvicorn sqlalchemy sqladmin pydantic[email]
    ```

2.  **Start the server**
    ```bash
    uvicorn main:app --reload
    ```

3.  **That's it!** The API is now running at `http://127.0.0.1:8000`.

## Features & Routes

Here is what you can do with the API:

| Method | Route | Action |
| :--- | :--- | :--- |
| `GET` | `/students/` | View all students |
| `POST` | `/students/` | Add a new student |
| `PUT` | `/students/{id}` | Update info |
| `DELETE` | `/students/{id}` | Remove student |

### Admin Dashboard
This project comes with a pre-built GUI to manage your database.
**Go to:** `http://127.0.0.1:8000/admin`

### API Docs
Automatic documentation is generated for you.
**Swagger UI:** `http://127.0.0.1:8000/docs`

## JSON Example
To create a student, send this JSON to the `POST` route:

```json
{
  "name": "Ali Hassan",
  "age": 21,
  "department": "Artificial Intelligence",
  "semester": 5,
  "email": "ali123@gmail.com"
}
