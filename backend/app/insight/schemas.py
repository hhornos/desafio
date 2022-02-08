#pylint: disable=E0611
#pylint: disable=R0903
"""app.event.schemas
Module that contains the event endpoint api contracts
"""
from datetime import datetime
from typing import List
from pydantic import BaseModel


class TagBase(BaseModel):
    ''' Tag Base Schema '''
    name: str


class TagResponse(TagBase):
    ''' Tag Response Schema '''
    id: int

    class Config:
        ''' Config Schema - orm_mode=True'''
        orm_mode = True
        


class TagRequest(TagBase):
    ''' Tag Resques Schema '''


class CardBase(BaseModel):
    ''' CardBase Schema '''
    texto: str


class Card(CardBase):
    ''' Card Schema '''
    id: int
    data_criacao: datetime
    data_modificacao: datetime = None
    tags: List[TagResponse] = []

    class Config:
        ''' Config Schema - orm_mode=True'''
        orm_mode = True


class CardCreate(CardBase):
    ''' CardCreate Schema '''
    tags: List[int] = []

    class Config:
        ''' Config Schema - orm_mode=True'''
        orm_mode = True


class CardUpdate(CardCreate):
    ''' CardUpdate Schema '''
