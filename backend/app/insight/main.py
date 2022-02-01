"""app.user.main
Module that contains the user endpoint routes
"""
from typing import List
from datetime import timedelta

from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from stackdriver_formatter import logging

from app.insight import crud, models, schemas
from app.db_session import engine, get_db


models.Base.metadata.create_all(bind=engine)

ROUTER = APIRouter()
LOGGER = logging.getLogger(__name__)


@ROUTER.post("/insigths/tags/", response_model=schemas.TagResponse, status_code=status.HTTP_201_CREATED)
async def create_tag(
        new_tag: schemas.TagRequest,
        data_base: Session = Depends(get_db)):
    ''' create_tag function '''
    return await crud.create_tag(data_base=data_base, tag=new_tag)


@ROUTER.get("/insigths/tags/{name}", response_model=schemas.TagResponse, status_code=status.HTTP_200_OK)
async def read_tag(
        name: str,
        data_base: Session = Depends(get_db)):
    ''' read_tag function '''
    db_tag = await crud.get_tag(data_base, name = name)
    return db_tag


@ROUTER.delete("/insigths/tags/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tag(
        id: int,
        data_base: Session = Depends(get_db)):
    ''' read_delete function '''
    await crud.delete_tag(data_base, id=id)


@ROUTER.put("/insigths/tags/{id}", response_model=schemas.TagResponse, status_code=status.HTTP_200_OK)
async def update_tag(
        id: int,
        tag: schemas.TagRequest,
        data_base: Session = Depends(get_db)):
    ''' read_update function '''
    db_tag = await crud.update_tag(data_base, id=id, tag=tag)
    if db_tag is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found")
    return db_tag


@ROUTER.post("/insigths/cards/", response_model=schemas.Card)
async def create_card(
        new_card: schemas.CardCreate,
        data_base: Session = Depends(get_db)):
    ''' create_tag function '''
    return await crud.create_card(data_base=data_base, card=new_card)


@ROUTER.get("/insigths/cards/{id}", response_model=schemas.Card)
async def read_card(
        id: int,
        data_base: Session = Depends(get_db)):
    ''' read_tag function '''
    db_card = await crud.get_card(data_base, id=id)
    if db_card is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Card not found")
    return db_card


@ROUTER.get("/insigths/cards/", response_model=schemas.Card)
async def list_card(
        skip: int,
        limit: int,
        data_base: Session = Depends(get_db)):
    ''' read_tag function '''
    return await crud.get_cards(data_base, skip=skip, limit=limit)


@ROUTER.delete("/insigths/cards/{id}", response_model=None)
async def delete_card(
        id: int,
        data_base: Session = Depends(get_db)):
    ''' read_delete function '''
    await crud.delete_card(data_base, id=id)


@ROUTER.put("/insigths/cards/{id}", response_model=schemas.Card)
async def update_card(
        id: int,
        card: schemas.CardUpdate,
        data_base: Session = Depends(get_db)):
    ''' read_update function '''
    return await crud.update_card(data_base, id=id, card=card)
