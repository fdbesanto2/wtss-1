from bdc_core.decorators.validators import require_model
from bdc_core.utils.flask import APIResource
from bdc_wtss.schemas import coverage_list, \
                                coverage_list_response, \
                                describe_coverage, \
                                describe_coverage_response, \
                                time_series
from flask_restplus import Namespace


api = Namespace('wtss', description='status')


@api.route('/list_coverages')
class ListCoverageController(APIResource):
    @require_model(coverage_list)
    def get(self):
        return {
            "coverages": []
        }


@api.route('/describe_coverage')
class DescribeCoverage(APIResource):
    @require_model(describe_coverage)
    def get(self):
        return {}


@api.route('/time_series')
class TimeSeries(APIResource):
    @require_model(time_series)
    def get(self):
        return {}