import unittest

from pyramid import testing

import transaction

import pep8
import logging
import os

logging.basicConfig()
log = logging.getLogger(__file__)
here = os.path.dirname(os.path.abspath(__file__))


def dummy_request(dbsession):
    return testing.DummyRequest(dbsession=dbsession)


class TestCodeFormat(unittest.TestCase):
    def test_pep8_conformance(self):
        log.warning('PEP8 Test')
        pep8style = pep8.StyleGuide()
        result = pep8style.check_files(['motmom/views/default.py',
                                        'motmom/views/auth.py',
                                        'motmom/security.py',
                                        'motmom/services/orderservice.py',
                                        'motmom/tests.py'])
        self.assertEqual(result.total_errors, 0,
                         'Found code style errors (and warnings).')
