from bdc_wtss.schemas import coverage_list, \
                                  coverage_list_response, \
                                  describe_coverage, \
                                  describe_coverage_response, \
                                  time_series
from bdc_wtss.utils.helpers import requires_model, APIResource
from flask_restplus import Namespace


api = Namespace('wtss', description='status')


@api.route('/list_coverages')
class ListCoverageController(APIResource):
    @requires_model(coverage_list)
    def get(self):
        return {
            "coverages": []
        }


@api.route('/describe_coverage')
class DescribeCoverage(APIResource):
    @requires_model(describe_coverage)
    def get(self):
        return {}


@api.route('/time_series')
class TimeSeries(APIResource):
    @requires_model(time_series)
    def get(self):
        return {}