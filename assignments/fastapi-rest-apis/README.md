# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API with FastAPI to practice route creation, request validation, status codes, and CRUD operations using an in-memory data store.

## 📝 Tasks

### 🛠️ Create Core API Endpoints

#### Description
Create a FastAPI application that exposes endpoints to manage a collection of books. Implement basic routes for reading and creating book records.

#### Requirements
Completed program should:

- Create a FastAPI app and run it with uvicorn.
- Implement `GET /health` that returns a JSON object confirming the API is running.
- Implement `GET /books` that returns a list of books.
- Implement `POST /books` that accepts book data and adds a new book to the in-memory list.
- Return correct HTTP status codes, including `201 Created` for successful creation.

### 🛠️ Add Update, Delete, and Validation

#### Description
Extend the API with full CRUD behavior. Use Pydantic models for request and response validation and handle missing records with proper error responses.

#### Requirements
Completed program should:

- Define a Pydantic model with fields: `id`, `title`, `author`, and `published_year`.
- Implement `GET /books/{book_id}` to return a single book by ID.
- Implement `PUT /books/{book_id}` to update an existing book.
- Implement `DELETE /books/{book_id}` to remove a book.
- Return `404 Not Found` when a requested book ID does not exist.
- Validate input so `published_year` is a positive integer.
