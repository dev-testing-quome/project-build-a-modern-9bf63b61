from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas import ProductCreate, Product
from services.product_service import create_product, get_products # Import your service functions

router = APIRouter(prefix="/api/products", tags=['Products'])

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Product, status_code=201)
def create_product_route(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(product, db)

@router.get("/", response_model=list[Product])
def get_products_route(db: Session = Depends(get_db)):
    return get_products(db)
