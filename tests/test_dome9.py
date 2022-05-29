import pytest
import os
from dome9 import Dome9

# ---------------- CREDENTIALS -----------------

# Credentials are set
def test_setting_arg_credentials():
    d9 = Dome9('U53RN4M3', 'P455W0RD')
    assert d9.key == "U53RN4M3"
    assert d9.secret == "P455W0RD"

# Args credentials > Env credentials
def test_setting_env_credentials():
    os.environ['DOME9_ACCESS_KEY'] = 'U53RN4M3'
    os.environ['DOME9_SECRET_KEY'] = 'P455W0RD'
    d9 = Dome9()
    assert d9.key == "U53RN4M3"
    assert d9.secret == "P455W0RD"

# Args credentials > Env credentials
def test_setting_both_credentials():
    os.environ['DOME9_ACCESS_KEY'] = 'InvalidUsername'
    os.environ['DOME9_SECRET_KEY'] = 'InvalidPassword'
    d9 = Dome9('U53RN4M3', 'P455W0RD')
    assert d9.key == "U53RN4M3"
    assert d9.secret == "P455W0RD"

# Show message if no credentials are set
def test_wrong_credentials():
    os.environ['DOME9_ACCESS_KEY'] = ''
    os.environ['DOME9_SECRET_KEY'] = ''
    with pytest.raises(ValueError):
        d9 = Dome9()

# Test using a different endpoint or api version
def test_setting_endpoint():
    d9 = Dome9('U53RN4M3', 'P455W0RD', endpoint='http://localhost:8000', apiVersion='v12')
    assert d9.endpoint == "http://localhost:8000/v12/"

# ---------------- REQUESTS -----------------

@pytest.fixture
def dome9():
    dome9 = Dome9('U53RN4M3', 'P455W0RD')
    return dome9

def test_get_requests(mocker, dome9):
    mocker.patch('requests.get',
        return_value=mocker.Mock(status_code=200, json=lambda: {'foo': 'bar'}))
    x = dome9._get('/random_URI')
    assert x['foo'] == 'bar'

def test_post_requests(mocker, dome9):
    mocker.patch('requests.post',
        return_value=mocker.Mock(status_code=200, json=lambda: {'foo': 'bar'}))
    x = dome9._post('/random_URI')
    assert x['foo'] == 'bar'

def test_put_requests(mocker, dome9):
    mocker.patch('requests.put',
        return_value=mocker.Mock(status_code=200, json=lambda: {'foo': 'bar'}))
    x = dome9._put('/random_URI')
    assert x['foo'] == 'bar'

def test_patch_requests(mocker, dome9):
    mocker.patch('requests.patch',
        return_value=mocker.Mock(status_code=200, json=lambda: {'foo': 'bar'}))
    x = dome9._patch('/random_URI')
    assert x['foo'] == 'bar'

def test_delete_requests(mocker, dome9):
    mocker.patch('requests.delete',
        return_value=mocker.Mock(status_code=204, json=lambda: {'foo': 'bar'}))
    x = dome9._delete('/random_URI')
    assert x == True