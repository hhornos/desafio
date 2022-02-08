#pylint: disable=R0903
"""app.user.models
Module that contains the user database models
"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship

from app.db_session import Base

card_tag_association_table = Table('card_tag_association_table', Base.metadata,
    Column('tag_id', ForeignKey('tag.id')),
    Column('card_id', ForeignKey('card.id'))
)

class Tag(Base):
    ''' Tag Model '''
    __tablename__ = "tag"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(40), unique=True)


class Card(Base):
    ''' Card Model '''
    __tablename__ = "card"

    id = Column(Integer, primary_key=True, index=True)
    texto = Column(String(400))
    data_criacao = Column(DateTime, default=datetime.utcnow)
    data_modificacao = Column(DateTime)
    
    tags = relationship("Tag",
                    secondary=card_tag_association_table)
