"""app.user.crud
Module that contains the user database crud functions
"""
from cgitb import text
from datetime import datetime
from tkinter.messagebox import NO

from sqlalchemy.orm import Session
from sqlalchemy import exc as db_exceptions

from app.insight import models, schemas
from app import exceptions as app_exceptions


async def create_tag(data_base: Session, tag: schemas.TagRequest):
    ''' create_tag funcion '''
    db_tag = models.Tag(**tag.dict())

    try:
        data_base.add(db_tag)
        data_base.commit()
        data_base.refresh(db_tag)
        return db_tag

    except db_exceptions.IntegrityError as ex:
        if ex.orig.args[0] == 1062: # Duplicate entry
            data_base.rollback()
            raise app_exceptions.AlreadyExists()
    


async def get_tag(data_base: Session, name: str):
    ''' get_tag funcion '''
    db_tag = data_base.query(models.Tag).filter(models.Tag.name == name).first()
    if db_tag is None:
        raise app_exceptions.NotFound()

    return db_tag


async def delete_tag(data_base: Session, id: int):
    ''' delete_tag funcion '''
    db_tag = data_base.query(models.Tag).get(id)
    if db_tag is None:
        raise app_exceptions.NotFound()

    try:
        data_base.query(models.Tag).filter(models.Tag.id == id).delete()

    except Exception as ex:
        data_base.rollback()
        raise ex
    
    data_base.commit()


async def update_tag(data_base: Session, id: int, tag: schemas.TagRequest):
    ''' update_tag funcion '''
    filtered_tags = data_base.query(models.Tag).filter(models.Tag.id == id)
    if filtered_tags.update(tag.__dict__) <= 0:
        data_base.rollback()
        raise app_exceptions.NotFound()

    data_base.commit()
    return filtered_tags.first()
        


async def create_card(data_base: Session, card: schemas.CardCreate):
    ''' create_card funcion '''
    print(card.tags)
    minhas_tags = data_base.query(models.Tag).filter(models.Tag.id.in_(card.tags)).all()
    if minhas_tags.__len__() != card.tags.__len__():
        raise app_exceptions.ListEntityNotFound()

    db_card = models.Card(
        texto=card.texto,
        tags=data_base.query(models.Tag).filter(models.Tag.id.in_(card.tags)).all()
    )

    data_base.add(db_card)
    data_base.commit()
    data_base.refresh(db_card)
    return db_card

# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item


async def get_card(data_base: Session, id: int):
    ''' get_card funcion '''
    return data_base.query(models.Card).get(id)


async def get_cards(data_base: Session, skip: int = 0, limit: int = 500):
    ''' get_cards funcion '''
    return data_base.query(models.Card).offset(skip).limit(limit).all()


async def delete_card(data_base: Session, id: int):
    ''' delete_tag funcion '''
    data_base.query(models.Card).delete(id)
    data_base.commit()


async def update_card(data_base: Session, id: int, card: schemas.CardUpdate):
    ''' update_tag funcion '''
    db_card = data_base.query(models.Card).get(id)
    db_card.text = card.texto
    db_card.tags = card.tags
    db_card.modified = datetime.now()
    data_base.query(models.Card).update(db_card)
    data_base.commit()
    return db_card

