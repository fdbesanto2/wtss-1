from bdc_wtss import app as wtss_app
import unittest


class TestListCoverage(unittest.TestCase):
    def setUp(self):
        app = wtss_app.test_client()
        self.response = app.get('/wtss/list_coverages')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)