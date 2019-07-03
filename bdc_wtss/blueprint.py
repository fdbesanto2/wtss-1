from bdc_wtss.controller import api as wtss_ns
from flask import Blueprint
from flask_restplus import Api


blueprint = Blueprint('bdc_wtss', __name__)

api = Api(blueprint, doc='')

api.add_namespace(wtss_ns)