""" Find all unit tests here """

import unittest
from io import BytesIO

from flask_testing import TestCase

import util
from app import APP
from constants import SAMPLE_LOG, LOG_PATTERN

class TestUtil(unittest.TestCase):
    """ Unit tests for util module """

    def test_convert_log_to_dict(self):
        """
            Test case of convert_log_to_dict function
        """
        assert isinstance(util.convert_log_to_dict(LOG_PATTERN, SAMPLE_LOG), dict)

    def test_is_indian_ip(self):
        """
            Test case of is_indian_ip
        """
        assert not util.is_indian_ip("1.1.1.1")
        assert util.is_indian_ip("117.196.40.28")


class FlaskAppTests(TestCase):
    """ Unit tests for the routes of flask app """

    render_templates = False

    def create_app(self):
        """
            Setup like method that does job of initilzation of flask instance
        """
        APP.debug = True
        return APP

    def test_index_route(self):
        """ tests index route to make sure templates runs without error"""
        self.client.get('/')
        self.assert_template_used('index.html')

    def test_process_log_api(self):
        """ tests process_log api """
        log_file = open('./sample.log', "rb")
        payload = {'log_file': (BytesIO(log_file.read()), 'log_file.log')}
        response = self.client.post('/api/process_log',
                                    data=payload,
                                    content_type='multipart/form-data')
        assert response.status_code == 200
        log_file.close()

if __name__ == '__main__':
    unittest.main()
