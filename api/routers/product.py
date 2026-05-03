from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session
from ..controllers import product as controller
from ..schemas import product as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Products'],
    prefix="/products"
)


@router.post("/", response_model=schema.Product)
def create(request: schema.ProductCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/search", response_model=list[schema.Product])
def search_by_category(category: str, db: Session = Depends(get_db)):
    return controller.read_by_category(db, category=category)


@router.get("/", response_model=list[schema.Product])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{item_id}", response_model=schema.Product)
def read_one(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=item_id)


@router.put("/{item_id}", response_model=schema.Product)
def update(item_id: int, request: schema.ProductUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=item_id)


@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=item_id)
