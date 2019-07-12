"""
Brazil Data Cube Main Blueprint

This file configures application routes, adding namespaces
into global API object
"""

from flask import Blueprint
from flask_restplus import Api
from bdc_wtss.controller import api as wtss_ns


blueprint = Blueprint('bdc_wtss', __name__)

api = Api(blueprint, doc='')

api.add_namespace(wtss_ns)
