# 🛒 E-commerce Product Catalog API

A complete FastAPI backend for managing products and categories in an e-commerce platform.

---

## ✅ Features

- CRUD for **Products** and **Categories**
- **SQLite + SQLAlchemy ORM**
- ✅ Input validation using **Pydantic**
- ✅ Supports **partial updates** (`PATCH`)
- ✅ Pagination for listing endpoints
- 🧪 Interactive API docs at `/docs`

## 🚀 Getting Started
### 1. Clone the Repository

### bash
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

  
# 🗂️ CATEGORY CRUD
### ✅ Create Category (with description)
 curl -X POST http://127.0.0.1:8000/categories/ ^
-H "Content-Type: application/json" ^
-d "{\"name\": \"Electronics\", \"description\": \"Electronic gadgets and devices\"}"

curl -X POST http://127.0.0.1:8000/categories/ ^
-H "Content-Type: application/json" ^
-d "{\"name\": \"Books\", \"description\": \"All kinds of books\"}"

curl -X POST http://127.0.0.1:8000/categories/ ^
-H "Content-Type: application/json" ^
-d "{\"name\": \"Clothing\", \"description\": \"Men's and Women's fashion\"}"

### 📋 List All Categories
curl http://127.0.0.1:8000/categories/

curl "http://127.0.0.1:8000/categories/?skip=0&limit=10"(with pagination)

### ✏️ Update Category (PATCH)
curl -X PATCH http://127.0.0.1:8000/categories/1 ^
-H "Content-Type: application/json" ^
-d "{\"name\": \"Gadgets\", \"description\": \"Updated category info\"}"

### 🗑️ Delete Category
curl -X DELETE http://127.0.0.1:8000/categories/2


# 📦 PRODUCT CRUD
### ✅ Create Product 
 curl -X POST http://127.0.0.1:8000/products/ ^
-H "Content-Type: application/json" ^
-d "{\"name\": \"Smartwatch\", \"description\": \"Fitness tracking watch\", \"price\": 199.99, \"stock\": 30, \"category_id\": 1}"

 curl -X POST http://127.0.0.1:8000/products/ ^
-H "Content-Type: application/json" ^
-d "{\"name\": \"Bluetooth Speaker\", \"description\": \"Portable wireless speaker\", \"price\": 89.99, \"stock\": 20, \"category_id\": 1}"

curl -X POST http://127.0.0.1:8000/products/ ^
-H "Content-Type: application/json" ^
-d "{\"name\": \"T-Shirt\", \"description\": \"Cotton unisex t-shirt\", \"price\": 19.99, \"stock\": 100, \"category_id\": 3}"

curl -X POST http://127.0.0.1:8000/products/ ^
-H "Content-Type: application/json" ^
-d "{\"name\": \"Jeans\", \"description\": \"Slim fit blue jeans\", \"price\": 49.99, \"stock\": 60, \"category_id\": 3}"


### 📋 List All Products
curl http://127.0.0.1:8000/products/

### 📃 List Products with Pagination ( pagination feature: skip 5, limit 5)
curl "http://127.0.0.1:8000/products/?skip=5&limit=5"

### 🔎 Get Product by ID
curl http://127.0.0.1:8000/products/1

### ✏️ Update Product (PATCH)
 curl -X PATCH http://127.0.0.1:8000/products/1 ^
-H "Content-Type: application/json" ^
-d "{\"name\": \"iPhone 13 Pro\", \"description\": \"Upgraded model\", \"price\": 899.99, \"category_id\": 3, \"stock\": 40}"
 
### 🗑️ Delete Product
curl -X DELETE http://127.0.0.1:8000/products/1

# 🧾 Products by Category 
curl http://127.0.0.1:8000/products/category/3

curl "http://127.0.0.1:8000/products/category/3?skip=0&limit=10"



