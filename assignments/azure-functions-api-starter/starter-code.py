import json
import azure.functions as func

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

# In-memory storage for this exercise only.
students = []


@app.route(route="health", methods=["GET"])
def health(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse(
        json.dumps({"status": "ok"}),
        status_code=200,
        mimetype="application/json",
    )


@app.route(route="hello", methods=["GET"])
def hello(req: func.HttpRequest) -> func.HttpResponse:
    name = req.params.get("name", "student")
    return func.HttpResponse(
        json.dumps({"message": f"Hello, {name}!"}),
        status_code=200,
        mimetype="application/json",
    )


@app.route(route="students", methods=["GET", "POST"])
def manage_students(req: func.HttpRequest) -> func.HttpResponse:
    if req.method == "GET":
        return func.HttpResponse(
            json.dumps(students),
            status_code=200,
            mimetype="application/json",
        )

    # TODO: Implement POST validation and create logic.
    # Expected fields: name (str), grade_level (int or str)
    # Return 400 for invalid input and 201 for created records.
    return func.HttpResponse(
        json.dumps({"error": "Not implemented yet"}),
        status_code=501,
        mimetype="application/json",
    )
