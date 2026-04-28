from datetime import datetime
from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import products as controller
from ..schemas import products as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Products'],
    prefix="/products"
)


@router.post("/", response_model=schema.Product)
def create(request: schema.ProductCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.Product])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/track/{tracking_number}", response_model=schema.Product)
def track_order(tracking_number: str, db: Session = Depends(get_db)):
    return controller.read_by_tracking(db, tracking_number=tracking_number)


@router.get("/filter", response_model=list[schema.Product])
def read_by_date_range(start_date: datetime, end_date: datetime, db: Session = Depends(get_db)):
    return controller.read_by_date_range(db, start_date=start_date, end_date=end_date)


@router.get("/{item_id}", response_model=schema.Product)
def read_one(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=item_id)


@router.put("/{item_id}", response_model=schema.Product)
def update(item_id: int, request: schema.ProductUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=item_id)


@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=item_id)
