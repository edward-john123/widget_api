# Widget REST API

A robust and well-tested RESTful API for managing "Widget" resources. Built with Python, Flask, SQLAlchemy, and Flask-Smorest for automatic OpenAPI (Swagger) documentation and data validation.

This project emphasizes clean code, comprehensive testing, and modern development practices including Dockerization, pre-commit hooks for linting/formatting, and CI/CD integration.

---

## ✨ Features

*   **CRUD Operations:** Full support for Creating, Reading, Listing, Updating, and Deleting Widgets.
*   **OpenAPI v3 Documentation:** Interactive API documentation and testing via Swagger UI, automatically generated.
*   **Data Validation:** Request and response data validation using Marshmallow schemas.
*   **Database:** Persistent storage using SQLite, managed with SQLAlchemy ORM and Flask-Migrate for schema migrations.
*   **Dockerized:** Easy setup and deployment using Docker and Docker Compose for both development and production-like environments (Gunicorn).
*   **Code Quality:**
    *   **Linting & Formatting:** Enforced by `ruff`, `black`, and `isort` via pre-commit hooks.
    *   **Security:** Automated security scanning with `bandit` in the CI pipeline.
*   **Testing:** Comprehensive unit tests using `pytest`, `Faker`, and `factory-boy`.
*   **CI/CD:** Integrated with GitHub Actions for automated testing and linting on every push/pull request.

---

## 🛠️ Tech Stack

*   **Backend:** Python 3.9+
*   **Framework:** Flask, Flask-Smorest
*   **ORM:** SQLAlchemy, Flask-SQLAlchemy
*   **Database:** SQLite (for simplicity, adaptable to others)
*   **Migrations:** Flask-Migrate (Alembic)
*   **Serialization/Validation:** Marshmallow, Flask-Marshmallow
*   **API Documentation:** OpenAPI 3 (Swagger UI)
*   **WSGI Server:** Gunicorn (for production-like environment)
*   **Testing:** Pytest, Faker, factory-boy
*   **Linting/Formatting:** Ruff, Black, Isort
*   **Security Scanning:** Bandit
*   **Containerization:** Docker, Docker Compose
*   **CI/CD:** GitHub Actions

---

## 🚀 Getting Started

### Prerequisites

*   Python 3.9+ & Pip
*   Docker & Docker Compose (Recommended for easiest setup)
*   Git

### 1. Clone the Repository

```bash
git clone https://github.com/edward-john123/widget_api.git
cd widget_api
```

### 2. Activate venv & Install requirement if not using Docker
```bash
python -m venv .venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate

# install requirement
pip install -r requirements.txt
```

### 3. Run the project (Docker, Dev, Prod)
```bash
FLASK_RUN_MODE="PROD" gunicorn run:app --bind 0.0.0.0:5000
FLASK_RUN_MODE="PROD" flask run
docker-compose up --build -d
```
Once up and running you can access Swagger-Ui via `0.0.0.0:5000/swagger-ui`

### 3. Run tests
```bash
# run all tests
pytest tests

# run tests wth coverage
pytest tests --cov=app --cov-report=html
```

### 4. Run pre-commit
The command below sets-up pre-commit locally and allows to run checks (ruff, black, isort, mypy & bandit)
```bash
pre-commit install
pre-commit run --all-files
```

### 💡 Possible Future Enhancements
- Authentication & Authorization (e.g., JWT)
- More sophisticated error handling and logging
- Rate limiting
- Support for other database backends (e.g., PostgreSQL)
- Caching strategies
- Pagination

### 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request or open an Issue.
Ensure that your contributions pass all pre-commit checks and unit tests.
