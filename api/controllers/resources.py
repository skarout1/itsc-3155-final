from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import resources as model
from ..models import recipes as recipe_model
from sqlalchemy.exc import SQLAlchemyError


def create(db: Session, request):
    new_item = model.Resource(**request.dict())
    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.__dict__['orig']))
    return new_item


def read_all(db: Session):
    return db.query(model.Resource).all()


def read_one(db: Session, item_id):
    item = db.query(model.Resource).filter(model.Resource.id == item_id).first()
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    return item


def update(db: Session, item_id, request):
    item = db.query(model.Resource).filter(model.Resource.id == item_id)
    if not item.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    item.update(request.dict(exclude_unset=True), synchronize_session=False)
    db.commit()
    return item.first()


def delete(db: Session, item_id):
    item = db.query(model.Resource).filter(model.Resource.id == item_id)
    if not item.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    item.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


def check_ingredients(db: Session, sandwich_id: int):
    recipes = db.query(recipe_model.Recipe).filter(recipe_model.Recipe.sandwich_id == sandwich_id).all()
    if not recipes:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No recipes found for this sandwich.")
    insufficient = []
    for r in recipes:
        resource = db.query(model.Resource).filter(model.Resource.id == r.resource_id).first()
        if resource and resource.amount < r.amount:
            insufficient.append({
                "resource": resource.item,
                "available": resource.amount,
                "required": r.amount
            })
    if insufficient:
        return {"status": "insufficient", "items": insufficient}
    return {"status": "ok", "items": []}
