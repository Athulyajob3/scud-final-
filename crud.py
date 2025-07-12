from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
import models, schemas

# ----------- CATEGORY OPERATIONS -----------

def create_category(db: Session, category: schemas.CategoryCreate):
    new_category = models.Category(**category.dict())
    db.add(new_category)
    try:
        db.commit()
        db.refresh(new_category)
        return new_category
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Category with this name already exists.")

def get_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Category).offset(skip).limit(limit).all()

def update_category(db: Session, category_id: int, data: dict):
    category = db.query(models.Category).filter(models.Category.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    for field, value in data.items():
        setattr(category, field, value)
    db.commit()
    db.refresh(category)
    return category

def delete_category(db: Session, category_id: int):
    category = db.query(models.Category).filter(models.Category.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    db.delete(category)
    db.commit()
    return {"detail": "Category deleted successfully"}


# ----------- PRODUCT OPERATIONS -----------

def create_product(db: Session, product: schemas.ProductCreate):
    category = db.query(models.Category).filter(models.Category.id == product.category_id).first()
    if not category:
        raise HTTPException(status_code=400, detail="Category ID does not exist.")
    new_product = models.Product(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()

def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()

def update_product(db: Session, product_id: int, product_data: dict):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    for field, value in product_data.items():
        setattr(product, field, value)
    db.commit()
    db.refresh(product)
    return product

def delete_product(db: Session, product_id: int):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(product)
    db.commit()
    return {"detail": "Product deleted successfully"}

def get_products_by_category(db: Session, category_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Product).filter(models.Product.category_id == category_id).offset(skip).limit(limit).all()
