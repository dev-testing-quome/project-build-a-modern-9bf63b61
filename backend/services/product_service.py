from sqlalchemy.orm import Session
from schemas import ProductCreate, Product
from models import Product as ProductModel # Import your database model

def create_product(product: ProductCreate, db: Session):
    db_product = ProductModel(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return Product.from_orm(db_product)

def get_products(db: Session):
    products = db.query(ProductModel).all()
    return [Product.from_orm(product) for product in products]
