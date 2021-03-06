def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('product_list', '/products')
    config.add_route('add_to_order', '/toorder/{id}')
    config.add_route('cart', '/cart')
    config.add_route('create_order', '/createorder')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    config.add_route('register', '/register')
    config.add_route('bid_list', '/myorders')
    config.add_route('delete_order', '/delete/{id}')
    config.add_route('report', '/report')
    config.add_route('order_list', '/reportorders')
    config.add_route('home', '/')

