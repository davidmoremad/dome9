import pytest
from . import dome9, mymock

def test_get_cloud_account(mocker, dome9):
    mymock(mocker, 'requests.get', 'CloudAccount.json', 200)
    x = dome9.get_cloud_account('1234567890')
    assert x['id'] == '00000000-0000-0000-0000-000000000000'


def test_list_cloud_accounts(mocker, dome9):
    mymock(mocker, 'requests.get', 'CloudAccounts.json', 200)
    x = dome9.list_cloud_accounts()
    assert isinstance(x, list)
    assert x[0]['id'] == '00000000-0000-0000-0000-000000000000'


def test_list_aws_accounts(mocker, dome9):
    mymock(mocker, 'requests.get', 'CloudAccounts.json', 200)
    x = dome9.list_aws_accounts()
    assert len(x) == 4
    assert next(filter(lambda z: z['vendor'] == 'aws', x))


def test_list_azure_accounts(mocker, dome9):
    mymock(mocker, 'requests.get', 'CloudAccounts.json', 200)
    x = dome9.list_azure_accounts()
    assert next(filter(lambda z: z['vendor'] == 'azure', x))


def test_list_google_accounts(mocker, dome9):
    mymock(mocker, 'requests.get', 'CloudAccounts.json', 200)
    x = dome9.list_google_accounts()
    assert next(filter(lambda z: z['vendor'] == 'google', x))


def test_list_kubernetes_accounts(mocker, dome9):
    mymock(mocker, 'requests.get', 'CloudAccounts.json', 200)
    x = dome9.list_kubernetes_accounts()
    assert next(filter(lambda z: z['vendor'] == 'kubernetes', x))


def test_connect_aws_account(mocker, dome9):
    mymock(mocker, 'requests.post', 'CloudAccount.json', 200)
    x = dome9.connect_aws_account('accountName', 'MYS3CR3T', 'arn:123456789:role/myrole')
    assert x['id'] == '00000000-0000-0000-0000-000000000000'
    

def test_connect_azure_account(mocker, dome9):
    mymock(mocker, 'requests.post', 'CloudAccount.json', 200)
    x = dome9.connect_azure_account(
        name='Testname',
        tenantId='b1b2b3b4-abcd-1234-1234-7bc77bc7',
        subscriptionId='b1b2b3b4-abcd-1234-1234-7bc77bc7',
        applicationId='b1b2b3b4-abcd-1234-1234-7bc77bc7',
        secretKey='qwertyuiopoiuytrewq'
    )
    assert x['id'] == '00000000-0000-0000-0000-000000000000'

