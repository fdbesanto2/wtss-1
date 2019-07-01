from bdc_wtss import app as wtss_app
from bdc_wtss.wtss.schemas import coverage_list_response, describe_coverage_response, time_series_response
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

        coverage_response = json_loads(self.response.data.decode('utf-8'))

        validate(instance=coverage_response, schema=coverage_list_response)


class TestDescribeCoverage(unittest.TestCase):
    def test_get_without_required_parameters(self):
        resp = app.get('/wtss/describe_coverage')
        self.assertEqual(400, resp.status_code)
        self.assertEqual(resp.content_type, 'application/json')

        coverage_response = json_loads(resp.data.decode('utf-8'))

        self.assertEqual(400, coverage_response['code'])
        self.assertEqual("\'name\' is a required property", coverage_response['message'])

    def test_get_with_required_parameters(self):
        resp = app.get('/wtss/describe_coverage?name=coverage')

        self.assertEqual(200, resp.status_code)
        self.assertEqual(resp.content_type, 'application/json')

    def test_get_response_validate_json_schema(self):
        resp = app.get('/wtss/describe_coverage?name=coverage')

        coverage_response = json_loads(resp.data.decode('utf-8'))

        validate(instance=coverage_response, schema=describe_coverage_response)


class TestTimeSeries(unittest.TestCase):
    @staticmethod
    def make_request(**properties):
        """
        Builds Flask Request object with properties values which generates query string args
        :param properties: Properties to pass to time series request. Each parameter represents query string args
        :return:
        """
        query_string = ""

        if len(properties.keys()) > 0:
            query_string = "?" + "&".join(['{}={}'.format(key, value) for (key, value) in properties.items()])

        return app.get('/wtss/time_series{}'.format(query_string))

    def wrap_missing_parameters_request(self, **properties):
        """
        Helper to validate error request of WTSS Time Series Service

        It already validates resp message code. **You must validate message code**

        :param properties: Properties to pass to time series request. Each parameter represents query string args
        :return: Tuple with Flask Response object and parsed JSON response data
        """
        resp = TestTimeSeries.make_request(**properties)

        self.assertEqual(400, resp.status_code)
        self.assertEqual(resp.content_type, 'application/json')
        coverage_response = json_loads(resp.data.decode('utf-8'))
        self.assertEqual(400, coverage_response['code'])

        return resp, coverage_response

    def test_get_without_coverage(self):
        resp = TestTimeSeries.make_request()

        self.assertEqual(400, resp.status_code)
        self.assertEqual(resp.content_type, 'application/json')

        coverage_response = json_loads(resp.data.decode('utf-8'))

        self.assertEqual(400, coverage_response['code'])

    def test_get_without_bbox(self):
        resp, data = self.wrap_missing_parameters_request(
            coverage='fake_coverage',
            start_date='2018-01-01',
            attributes='nir,nvdi'
        )

        self.assertEqual("'latitude' is a required property", data['message'])

        resp, data = self.wrap_missing_parameters_request(
            coverage='fake_cube',
            start_date='2018-01-01',
            attributes='nir,nvdi',
            latitude=-12.5
        )
        self.assertEqual("'longitude' is a required property", data['message'])

    def test_get_time_series(self):
        resp = TestTimeSeries.make_request(
            coverage="fake_cube",
            start_date='2018-01-01',
            end_date='2019-01-01',
            attributes='nir,nvdi',
            latitude=-12.5,
            longitude=-48
        )

        self.assertEqual(200, resp.status_code)

        time_series_result = json_loads(resp.data.decode('utf-8'))

        validate(instance=time_series_result, schema=time_series_response)