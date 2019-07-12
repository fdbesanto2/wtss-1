"""Controllers of Web Time Series Service

The WTSS consists in three operations:
    - `wtss/list_coverages` Retrieve List of Coverage Offered
    - `wtss/describe_coverage` Retrieve Coverage metadata
    - `wtss/time_series` Retrieve time series from location given
"""

from flask_restplus import Namespace
from bdc_core.decorators.validators import require_model
from bdc_core.utils.flask import APIResource
from bdc_wtss.schemas import coverage_list, \
                                describe_coverage, \
                                time_series


api = Namespace('wtss', description='status')


@api.route('/list_coverages')
class ListCoverageController(APIResource):
    """WTSS ListCoverage Operation

    This method works only with GET operation.
    There is no required arguments for this operation, but
    you can find the JSON Schema structure at
    json-schemas/list_coverages_request.json
    """
    @require_model(coverage_list)
    def get(self):
        """
        Retrieve list of coverage offered

        Returns:
            str[]: List of coverage available in server
        """
        return {
            "coverages": []
        }


@api.route('/describe_coverage')
class DescribeCoverage(APIResource):
    """WTSS DescribeCoverage Operation

    This method works only with GET operation.
    The required argument is `name`, which represents coverage identifier.
    You can find the JSON Schema structure at
    json-schemas/list_coverages_request.json
    """
    @require_model(describe_coverage)
    def get(self):
        """
        Retrieves coverage metadata. These values can be spatio temporal limits,
        projection, attribute names and timeline.
        Returns:
            dict: Return Coverage Description
        """
        return {}


@api.route('/time_series')
class TimeSeries(APIResource):
    """
    WTSS DescribeCoverage Operation

    This method works only with GET operation. It will support
    POST method to retrieve time series of region of interest.
    There are a bunch of required arguments to execute this operation, such
    `coverage`, `attributes`, `latitude`, `longitude`, `start_date` and
    `end_date`. You can find the JSON Schema structure at
    json-schemas/list_coverages_request.json
    """
    @require_model(time_series)
    def get(self):
        """
        time_series coverage
        Returns:
            dict: Return coverage time series
        """
        return {}
