from pyramid.config import Configurator
from pyramid.session import UnencryptedCookieSessionFactoryConfig
from pyramid.security import Allow, Everyone

class Root(object):
    __acl__ = [(Allow, Everyone, 'view'),
               (Allow, 'developer', 'developer'),
               (Allow, 'baker', 'baker')]

    def __init__(self, request):
        pass

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        # session factory
        session_factory = UnencryptedCookieSessionFactoryConfig('itsaseekreet')
        # configuration setup
        config = Configurator(settings=settings, session_factory=session_factory, root_factory=Root)
        config.include('.security')
        config.include('.models')
        config.include('pyramid_mako')
        config.include('.routes')
        config.scan()
    return config.make_wsgi_app()
