from sanic import Blueprint
from .basic import basic

# from  sanic_openapi import openapi2_blueprint






blueprint_group = Blueprint.group(
    basic  
)