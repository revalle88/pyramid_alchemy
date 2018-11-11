from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    Text,
)
from sqlalchemy.orm import relationship

from .meta import Base


class Product(Base):
    """ The SQLAlchemy declarative model class for a Page object. """
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False, unique=True)
    price = Column(Integer, nullable=False)

