from bdc_wtss.config import BASE_DIR
from json import loads as json_loads
from pathlib import Path


# TODO: Get schemas by API Version
schemas_folder = Path(BASE_DIR).parent / 'spec/json-schemas/v1.0/operations'


def load_schema(file_name):
    """
    Open file and parses as JSON file
    :param file_name:
    :return:
    """
    schema_file = schemas_folder / file_name

    with schema_file.open() as f:
        return json_loads(f.read())


# Schemas
coverage_list = load_schema('list_coverages_request.json')
coverage_list_response = load_schema('list_coverages_response.json')
describe_coverage = load_schema('describe_coverage_request.json')
describe_coverage_response = load_schema('describe_coverage_response.json')
time_series = load_schema('time_series_request.json')
time_series_response = load_schema('time_series_response.json')