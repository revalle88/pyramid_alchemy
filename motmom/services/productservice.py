from ..models import User, Bid, Product
from .. import models
import sqlalchemy as sa
from sqlalchemy import func
import datetime


class Product_service(object):
    @classmethod
    def all(cls, request):
        query = request.dbsession.query(Product)
        return query.order_by(sa.asc(Product.id))

    @classmethod
    def get_products_in_cart(cls, request):
        session = request.session
        # order_items = ','.join(map(str, session['order_list']))
        order_items = session['order_list']
        products = request.dbsession.query(Product
            ).filter(Product.id.in_(order_items)).all()
        return products
