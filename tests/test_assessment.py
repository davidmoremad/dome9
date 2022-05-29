import pytest
from . import dome9, mymock

def test_get_assessment(mocker, dome9):
    file = mymock(mocker, 'requests.get', 'AssessmentResult.json', 200)
    assessment = dome9.get_assessment('1234')
    assert file == assessment

def test_run_assessment(mocker, dome9):
    file = mymock(mocker, 'requests.post', 'AssessmentResult.json', 200)
    assessment = dome9.run_assessment('1234', '00000000-0000-0000-0000-000000000000')
    assert file == assessment