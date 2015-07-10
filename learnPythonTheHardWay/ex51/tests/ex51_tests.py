from nose.tools import *
from bin.app import app
from tests.tools import assert_response # Using an absolute import here

def test_index():
    # check that we get a 404 on the / URL
    resp = app.request("/")
    assert_response(resp, status="404")
    
    # test initial GET request to /hello
    resp = app.request("/hello")
    assert_response(resp)
    
    # make sure default values work for the form
    resp = app.request("/hello", method="POST")
    assert_response(resp, contains="Nobody")
    
    # test that parameters can be passed
    data = {'name': 'self', 'msg': 'Hola'}
    resp = app.request("/hello", method="POST", data=data)
    assert_response(resp, contains="self")
    assert_response(resp, contains="Hola")
