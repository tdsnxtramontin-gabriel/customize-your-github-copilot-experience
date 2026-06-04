# 📘 Assignment: Azure Functions API Starter

## 🎯 Objective

Build a beginner-friendly HTTP API using Python Azure Functions. Students will practice creating cloud-style endpoints, returning JSON responses, and validating request data.

## 📝 Tasks

### 🛠️ Build Your First HTTP Function

#### Description
Set up a Python Azure Functions app with a health-check endpoint and a greeting endpoint. This task introduces the structure of a serverless API in the Microsoft ecosystem.

#### Requirements
Completed program should:

- Define a function app using the Azure Functions Python programming model.
- Implement `GET /api/health` that returns JSON like `{ "status": "ok" }`.
- Implement `GET /api/hello?name=...` that returns a personalized JSON greeting.
- Return `200 OK` responses with `application/json` content type.


### 🛠️ Add a Simple POST Endpoint with Validation

#### Description
Create a POST endpoint that accepts student data, validates required fields, and returns meaningful responses. This simulates common API patterns used in production services.

#### Requirements
Completed program should:

- Implement `POST /api/students` that accepts JSON with `name` and `grade_level`.
- Return `400 Bad Request` with an error message if either field is missing.
- Store valid student records in an in-memory list.
- Return `201 Created` with the created student record as JSON.
- Implement `GET /api/students` to return all saved records.
