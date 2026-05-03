from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session
from ..controllers import deals as controller
from ..schemas import deals as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Deals'],
    prefix="/deals"
)


@router.post("/", response_model=schema.Deal)
def create(request: schema.DealCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.Deal])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{item_id}", response_model=schema.Deal)
def read_one(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=item_id)


@router.put("/{item_id}", response_model=schema.Deal)
def update(item_id: int, request: schema.DealUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=item_id)


@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=item_id)
