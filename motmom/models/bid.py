from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    Text,
    Table,
    DateTime,
)
from sqlalchemy.orm import relationship

from .meta import Base

class Bid(Base):
    """ The SQLAlchemy declarative model class for a Page object. """
    __tablename__ = 'bids'
    id = Column(Integer, primary_key=True)
    data = Column(Text)
    price = Column(Integer)
    qrcode = Column(Text)
    comment = Column(Text)
    datetime = Column(DateTime)

    creator_id = Column(ForeignKey('users.id'), nullable=False)
    creator = relationship('User', backref='created_bids')



