from bdc_wtss import app as wtss_app
from bdc_wtss.wtss.schemas import coverage_list_response, describe_coverage_response
import unittest

from json import loads as json_loads
from jsonschema import validate


app = wtss_app.test_client()

class TestListCoverage(unittest.TestCase):
    def setUp(self):
        self.response = app.get('/wtss/list_coverages')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_response_format_with_json_schema(self):
        self.assertEqual(self.response.content_type, 'application/json')

        coverage_response = json_loads(self.response.data)

        validate(instance=coverage_response, schema=coverage_list_response)


class TestDescribeCoverageWithoutParameters(unittest.TestCase):
    def setUp(self):
        self.response = app.get('/wtss/describe_coverage')

    def test_get(self):
        self.assertEqual(400, self.response.status_code)

    def test_response(self):
        self.assertEqual(self.response.content_type, 'application/json')

        coverage_response = json_loads(self.response.data)

        self.assertEqual(400, coverage_response['code'])
        self.assertEqual("\'name\' is a required property", coverage_response['message'])


class TestDescribeCoverageWithParameters(unittest.TestCase):
    def setUp(self):
        self.response = app.get('/wtss/describe_coverage?name=coverage')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_response(self):
        self.assertEqual(self.response.content_type, 'application/json')

        coverage_response = json_loads(self.response.data)

        validate(instance=coverage_response, schema=describe_coverage_response)