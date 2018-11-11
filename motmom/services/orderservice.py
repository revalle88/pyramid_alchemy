from ..models import User, Bid, Product
from .. import models
import sqlalchemy as sa
from sqlalchemy import func
import datetime
import pyqrcode
import png
import os


class Order_service(object):
    @classmethod
    def all(cls, request):
        query = request.dbsession.query(Bid)
        return query.order_by(sa.desc(Bid.datetime))

    @classmethod
    def get_by_user(cls, request):
        bids = request.dbsession.query(Bid
                                       ).filter_by(creator=request.user).all()
        return bids

    @classmethod
    def get_by_period(cls, request, from_date, to_date):
        base_query = request.dbsession.query(
            User.name,
            func.sum(Bid.price).label('total')
        ).join(Bid.creator
               ).filter(Bid.datetime < to_date
                        ).filter(Bid.datetime > from_date
                                 ).group_by(User.name)
        records = [dict(username=row[0], total=row[1])
                   for row in base_query.all()]
        return records

    @classmethod
    def add(cls, request, data, price, comment):
        bid = Bid(data=data, price=price, comment=comment,
                  creator=request.user, datetime=datetime.datetime.now())
        request.dbsession.add(bid)
        request.dbsession.flush()
        request.dbsession.refresh(bid)
        bid_id = bid.id
        qr = pyqrcode.create(str(price)+str(bid.id))
        here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        qrpathos = os.path.join(here, 'static')+'\\qr\\qr'+str(bid_id)+'.png'
        qrpath = 'static/qr/qr'+str(bid.id)+'.png'
        try:
            qr.png(qrpathos, scale=5)
        except Exception as e:
            print(str(e))
        bid = request.dbsession.query(Bid).filter_by(id=bid_id).one()
        bid.qrcode = qrpath

    @classmethod
    def delete(cls, request, bid_id):
        request.dbsession.query(Bid).filter_by(id=bid_id).delete()
