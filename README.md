<h1 align="center">URL Shortener App:</h1>

![Status](https://img.shields.io/badge/Status-In_Development-yellow?style=for-the-badge
)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)

An API made with **Python** and **FastAPI** that allows shortening long URLs and redirecting to them through a short identifier. This project uses **Docker**, **Docker Compose**, **PostgreSQL**, **SQLAlchemy**, and **Alembic** for database management and infrastructure.

---

## 📦 Technologies Used

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Alembic](https://alembic.sqlalchemy.org/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [PostgreSQL](https://www.postgresql.org/)

---

## 🧪 API Endpoints

### `POST /shorten-url`

Shortens a provided URL.

**Request Body (JSON):**
```json
{
  "url": "https://example.com"
}
```

**Response (JSON):**
```json
{
  "url": "https://example.com",
  "short_url": "http://localhost:8000/abc123"
}
```

### `GET /{short_code}`

Redirects to the original URL associated with the shortened code.

* **Example:** Accessing `http://localhost:8000/abc123` will automatically redirect to `https://example.com`.

---

## 📄 Interactive Documentation

After running the application, access the automatically generated documentation by FastAPI at:

* [http://localhost:8000/docs](http://localhost:8000/docs) or [http://localhost:8000/redoc](http://localhost:8000/redoc)


## 🐳 How to Run with Docker Compose

### Prerequisites

* Docker
* Docker Compose

### Steps

1. Create a `.env` file in the project root with the following content:
```env
DB_NAME=url_shortener
DB_USER=postgres
DB_PASSWORD=postgres
DB_PORT=5432
DB_HOST=localhost
DB_DRIVER="postgresql+psycopg"
```

2. Run the following command to start the services:
```bash
docker-compose up --build
```
Docker Compose will automatically start:

* **db**: Container with the PostgreSQL database.
* **backend**: API with FastAPI.
* **alembic**: Runs the database migrations.

ℹ️ The file `compose.yaml` is already included in the repository.

---

## 📜 License

This project is licensed under the MIT license.

## 👤 Author

* Jean Gabriel Ferreira
* Github: [@FerreirinhaJean](https://github.com/FerreirinhaJean)