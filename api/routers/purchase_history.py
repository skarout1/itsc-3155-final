from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session
from ..controllers import purchase_history as controller
from ..schemas import purchase_history as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Purchase History'],
    prefix="/purchasehistory"
)


@router.post("/", response_model=schema.PurchaseHistory)
def create(request: schema.PurchaseHistoryCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.PurchaseHistory])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{item_id}", response_model=schema.PurchaseHistory)
def read_one(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=item_id)


@router.put("/{item_id}", response_model=schema.PurchaseHistory)
def update(item_id: int, request: schema.PurchaseHistoryUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=item_id)


@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=item_id)
