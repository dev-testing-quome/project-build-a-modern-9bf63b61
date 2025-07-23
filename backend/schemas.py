from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class User(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class ProductCreate(BaseModel):
    name: str
    description: str
    price: int
    image_url: str
    stock: int

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: int
    image_url: str
    stock: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class ReviewCreate(BaseModel):
    product_id: int
    rating: int
    comment: str

class Review(BaseModel):
    id: int
    product_id: int
    rating: int
    comment: Optional[str] = None
    created_at: datetime

    class Config:
        orm_mode = True

class OrderCreate(BaseModel):
    user_id: int
    order_items: List[dict]

class Order(BaseModel):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime
    order_items: List[dict] = []

    class Config:
        orm_mode = True

class OrderItem(BaseModel):
    id: int
    order_id: int
    product_id: int
    quantity: int

    class Config:
        orm_mode = True
