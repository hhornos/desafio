# pylint:disable=line-too-long
"""
Modulo to create a DB connection Session
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.configuration import DATABASE as cfg


def get_connection_string():
    """function to get db connection string"""

    if not cfg["host"] and not cfg["port"] and cfg["unix_socket"]:
        return f'{cfg["driver"]}://{cfg["user"]}:{cfg["password"]}@/{cfg["name"]}?unix_socket={cfg["unix_socket"]}'

    return f'{cfg["driver"]}://{cfg["user"]}:{cfg["password"]}@{cfg["host"]}:{cfg["port"]}/{cfg["name"]}'

engine = create_engine(
    get_connection_string(), pool_pre_ping=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)
Base = declarative_base()

# FAST API Dependency
def get_db():
    """Create a database fastapi dependency module"""
    db_session = SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close() # pylint:disable=no-member
