from pyramid.view import view_config
from pyramid.response import Response

from sqlalchemy.exc import DBAPIError
from sqlalchemy import func

from pyramid.httpexceptions import (
    HTTPForbidden,
    HTTPFound,
    HTTPNotFound,
    )

import pyqrcode
import png
import os
import pkg_resources

import datetime

from .. import models
from ..services.orderservice import Order_service
from ..services.productservice import Product_service

import logging
import os

logging.basicConfig()
log = logging.getLogger(__file__)
here = os.path.dirname(os.path.abspath(__file__))


# views
@view_config(route_name='home', renderer='../templates/home.mako')
def home(request):
    return {}


@view_config(route_name='product_list',
             renderer='../templates/product_list.mako',
             permission='developer')
def product_list(request):
    products = Product_service.all(request)
    return dict(products=products)


# add product to order
@view_config(route_name='add_to_order', permission='developer')
def add_to_order(request):
    bid_id = int(request.matchdict['id'])
    session = request.session
    if 'order_list' in session:
        session['order_list'].append(bid_id)
    else:
        session['order_list'] = [bid_id]
    return HTTPFound(location=request.route_url('product_list'))


@view_config(route_name='cart', renderer='../templates/cart.mako',
             permission='developer')
def cart_view(request):
    session = request.session
    message = ''
    bid_content = ''
    summ = 0
    if 'order_list' in session:
        products = Product_service.get_products_in_cart(request)
        for product in products:
            bid_content = bid_content + product.name + '; '
            summ = summ + product.price
        return dict(
            message=message,
            bid_content=bid_content,
            summ=summ,
            products=products,
            )
    else:
        message = "empty"
        return {'empty': 'empty'}


@view_config(route_name='bid_list', renderer='../templates/bid_list.mako',
             permission='developer')
def list_view(request):
    bids = Order_service.get_by_user(request)
    return {'bids': bids}


@view_config(route_name='create_order', permission='developer')
def create_order(request):
    if 'form.submitted' in request.params:
        price = request.params['price']
        data = request.params['data']
        comment = request.params['comment']
        Order_service.add(request, data, price, comment)
        del request.session['order_list']
        return HTTPFound(location=request.route_url('bid_list'))
    else:
            request.session.flash('Please enter a your meal list!')
    return HTTPFound(location=request.route_url('product_list'))


@view_config(route_name='delete_order', permission='baker')
def delete_order(request):
    bid_id = int(request.matchdict['id'])
    Order_service.delete(request, bid_id)
    request.session.flash('Bid was successfully deleted!')
    return HTTPFound(location=request.route_url('order_list'))


# baker views
@view_config(route_name='report',
             renderer='../templates/report.mako',
             permission='baker')
def report_view(request):
    from_date = ''
    to_date = ''
    if 'form.submitted' in request.params:
        from_date = request.params['from_date']
        to_date = request.params['to_date']
        format_s = '%Y-%m-%d'
        from_date_obj = datetime.datetime.strptime(from_date, format_s).date()
        to_date_obj = datetime.datetime.strptime(to_date, format_s).date()
    else:
        from_date_obj = datetime.date(2000, 1, 1)
        to_date_obj = datetime.datetime.now()
    records = Order_service.get_by_period(request, from_date_obj, to_date_obj)
    return {
            'records': records,
            'from_date': from_date,
            'to_date': to_date
            }


@view_config(route_name='order_list',
             renderer='../templates/order_list.mako',
             permission='baker')
def order_list(request):
    orders = Order_service.all(request)
    return {'orders': orders}
