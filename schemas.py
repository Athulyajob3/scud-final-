from pydantic import BaseModel, Field
from typing import Optional


# ----------- Category Schemas -----------

class CategoryBase(BaseModel):
    name: str = Field(..., example="Electronics")
    description: Optional[str] = Field(None, example="Devices and gadgets")

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True


# ----------- Product Schemas -----------

class ProductBase(BaseModel):
    name: Optional[str] = Field(None, example="Smartphone")
    description: Optional[str] = Field(None, example="Android phone")
    price: Optional[float] = Field(None, example=29999.99)
    stock: Optional[int] = Field(None, example=50)
    category_id: Optional[int] = Field(None, example=1)

class ProductCreate(ProductBase):
    name: str
    price: float
    stock: int
    category_id: int

class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True
