"""
This module WTSS Operations vocabularies. It is defined as `request` and `response` objects.

Attributes:
    coverage_list (dict): JSON Schema of WTSS list_coverages request

    coverage_list_response (dict): JSON Schema of WTSS list_coverages response

    describe_coverage (dict): JSON Schema of WTSS describe_coverage request operation

    describe_coverage_response (dict): JSON Schema of WTSS describe_coverage response operation

    time_series (dict): JSON Schema of WTSS time_series request operation

    time_series_response (dict): JSON Schema of WTSS time_series response operation
"""

from bdc_wtss.config import BASE_DIR
from json import loads as json_loads
from pathlib import Path


# TODO: Get schemas by API Version
schemas_folder = Path(BASE_DIR) / 'json-schemas/'


def load_schema(file_name):
    """
    Open file and parses as JSON file

    Args:
        file_name (str): File name of JSON Schema
    Returns:
        JSON schema parsed as Python object (dict)
    Raises:
        json.JSONDecodeError When file is not valid JSON object
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