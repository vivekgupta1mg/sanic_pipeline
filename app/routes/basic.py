from sanic import Blueprint, Sanic
from sanic.response import json



basic = Blueprint("basic", url_prefix="/basic")



@basic.route("/")
async def test(request):
    return json({"hello": "world"})