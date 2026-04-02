---
title: "Flask"
---

Flask

Resources:
- https://codefinity.com/blog/Top-50-Technical-Interview-Questions-for-Flask-Developers
- https://www.hirist.tech/blog/top-30-flask-interview-questions-and-answers/

Flask is a micro web framework for Python — lightweight, flexible, modular.

Basic App:
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home(): return "Hello, Flask!"

if __name__ == '__main__': app.run(debug=True)
```

Routes: @app.route('/user/<name>') for dynamic URLs
HTTP Methods: methods=['GET', 'POST']

Flask vs Django:
- Flask: micro-framework, highly flexible, minimal built-ins
- Django: full-stack, less flexible, ORM + auth + admin included

Key Features:

1. Templates (Jinja2): render_template('hello.html', name=name)
   - {{ name }}, {% if %}, {% for %}

2. WTForms: pip install flask-wtf
   - FlaskForm, StringField, SubmitField, DataRequired validator

3. SQLAlchemy:
```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
db = SQLAlchemy(app)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
```

4. Authentication: Flask-Login, UserMixin

5. Flask-RESTful:
```python
from flask_restful import Api, Resource
api = Api(app)
class HelloWorld(Resource):
    def get(self): return {"message": "Hello"}
api.add_resource(HelloWorld, '/api')
```

6. Sessions: session['username'] = 'john_doe'

7. Caching: @cache.cached(timeout=50)

8. Blueprints (modular apps):
```python
users_bp = Blueprint('users', __name__)
@users_bp.route('/profile')
def profile(): return "User Profile"
app.register_blueprint(users_bp, url_prefix='/users')
```

9. Middleware:
```python
@app.before_request
def before_request(): print(f"Request: {request.path}")
@app.after_request
def after_request(response): return response
```

Scaling:
- Production server: gunicorn or uWSGI
- Caching: Flask-Caching
- Load balancing: Nginx + multiple Flask instances
- Async: Celery for background tasks
- DB: indexing, connection pooling

Concurrency: Flask is single-threaded by default.
- gunicorn -w 4 app:app for concurrent requests
- gevent or eventlet for async networking
