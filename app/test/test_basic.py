from sanic import Blueprint, Sanic
from sanic.response import json
from unittest import TestCase
import unittest
from ..routes.basic import basic

app = Sanic(__name__)
app.blueprint(basic)


class TestValidation(TestCase):
    def test_1(self):
        
        request,response = app.test_client.post('/basic/', 
                                                headers={"Content-Type":"application/json"})
        assert response.status == 200


if __name__ == "__main__":
    unittest.main()