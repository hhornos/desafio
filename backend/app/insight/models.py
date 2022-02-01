#pylint: disable=R0903
"""app.user.models
Module that contains the user database models
"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.db_session import Base


class Tag(Base):
    ''' Tag Model '''
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(40), unique=True)


class Card(Base):
    ''' Card Model '''
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String(400))
    created = Column(DateTime, default=datetime.utcnow)
    modified = Column(DateTime)
    tag_id = Column(Integer, ForeignKey("tags.id"))

    tags = relationship(Tag)
