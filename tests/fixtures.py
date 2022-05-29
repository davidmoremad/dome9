import pytest
import json
from dome9 import Dome9

@pytest.fixture
def dome9():
    dome9 = Dome9('U53RN4M3', 'P455W0RD')
    return dome9

def mymock(mocker, function, mockFile, status_code):
    mock = json.loads(open(f'tests/mocks/{mockFile}', 'r').read())
    mocker.patch(function, return_value=mocker.Mock(status_code=status_code, json=lambda: mock))
    return mock
