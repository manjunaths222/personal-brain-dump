---
title: "Fastapi"
---

FastAPI

Resource: https://www.vskills.in/certification/tutorial/top-50-fastapi-job-interview-questions-and-answer/

What is FastAPI:
Modern, high-performance Python web framework (3.7+) based on type hints.
Built on: Starlette (web handling) + Pydantic (data validation).
Features: async/await, auto-generated OpenAPI docs, built-in validation, dependency injection, fast (comparable to Node.js/Go).

Install: pip install fastapi uvicorn
Run: uvicorn main:app --reload

Key Concepts:

1. Path & Query Parameters:
```python
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
```

2. Request Body & Pydantic Models:
```python
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = False

@app.post("/items/")
def create_item(item: Item): return {"item": item}
```

3. Response Models: response_model=ItemOut ensures only specified fields returned

4. HTTP Methods: @app.get, @app.post, @app.put, @app.delete, @app.patch

5. Status Codes: status_code=status.HTTP_201_CREATED

6. Dependency Injection:
```python
def common_params(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

@app.get("/items/")
def read_items(params: dict = Depends(common_params)):
    return params
```

7. Authentication: OAuth2PasswordBearer, JWT via fastapi.security

8. File Uploads:
```python
@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}
```

9. Background Tasks:
```python
def write_log(msg): ...
@app.post("/notify/")
def notify(background_tasks: BackgroundTasks):
    background_tasks.add_task(write_log, "Notification sent")
```

10. Middleware: CORSMiddleware, custom middleware via app.add_middleware

11. Exception Handling: raise HTTPException(status_code=404, detail="Not found")

12. Database: SQLAlchemy + async_session, Alembic for migrations

13. Testing:
```python
client = TestClient(app)
def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
```

14. Auto Docs: /docs (Swagger UI), /redoc (ReDoc)

Deployment: Uvicorn + Gunicorn, Docker, AWS Lambda (via Mangum), Render/Railway/Vercel

vs Flask/Django:
- FastAPI: async, auto-validation, auto-docs, type hints, high performance
- Flask: simpler, sync by default, more flexibility
- Django: batteries included, ORM, admin panel

Real-world Use Cases:
- REST API with SQLAlchemy + JWT auth
- Webhook receivers (Stripe, GitHub)
- ML model serving backend
- Multi-tenant SaaS backend
- Role-based access control APIs
