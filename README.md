# 🛒 E-commerce Product Catalog API

A complete FastAPI backend for managing products and categories in an e-commerce platform.

---

## ✅ Features

- CRUD for **Products** and **Categories**
- **SQLite + SQLAlchemy ORM**
- ✅ Input validation using **Pydantic**
- ❌ Handles duplicate category errors
- ✅ Supports **partial updates** (`PATCH`)
- ✅ Pagination for listing endpoints
- 🧪 Interactive API docs at `/docs`

---

## 📁 Project Structure


## 🚀 Getting Started
### 1. Clone the Repository

```bash
git clone https://github.com/athulyajob3/scudapp.git
cd scudapp

### Create and Activate Virtual Environment
python -m venv env
env\Scripts\activate   # Windows

### Install Dependencies
pip install -r requirements.txt

### Start the FastAPI Server
python -m uvicorn main:app --reload

### The server will start at:
http://127.0.0.1:8000/docs

### You can test the API using the built-in Swagger UI:
📘 Swagger UI → http://127.0.0.1:8000/docs
📕 ReDoc UI → http://127.0.0.1:8000/redoc

 

