from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="🛒 E-commerce Product Catalog API")


# ----------- Dependency ----------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ----------- Category Endpoints -----------

@app.post("/categories/", response_model=schemas.Category)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db, category)

@app.get("/categories/", response_model=List[schemas.Category])
def list_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_categories(db, skip=skip, limit=limit)

@app.patch("/categories/{id}", response_model=schemas.Category)
def update_category(id: int, data: dict, db: Session = Depends(get_db)):
    return crud.update_category(db, id, data)

@app.delete("/categories/{id}")
def delete_category(id: int, db: Session = Depends(get_db)):
    return crud.delete_category(db, id)


# ----------- Product Endpoints -----------

@app.post("/products/", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, product)

@app.get("/products/", response_model=List[schemas.Product])
def list_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_products(db, skip=skip, limit=limit)

@app.get("/products/{id}", response_model=schemas.Product)
def get_product(id: int, db: Session = Depends(get_db)):
    db_product = crud.get_product(db, id)
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@app.get("/products/category/{category_id}", response_model=List[schemas.Product])
def list_by_category(category_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_products_by_category(db, category_id, skip=skip, limit=limit)

@app.patch("/products/{id}", response_model=schemas.Product)
def patch_product(id: int, data: dict, db: Session = Depends(get_db)):
    return crud.update_product(db, id, data)

@app.delete("/products/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    return crud.delete_product(db, id)
