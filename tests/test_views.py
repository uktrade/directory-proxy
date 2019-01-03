import json
import urllib3
from unittest import mock

import pytest


@mock.patch('urllib3.poolmanager.PoolManager.urlopen')
def test_pass_through(mock_urlopen, client, settings):
    mock_urlopen.return_value = urllib3.response.HTTPResponse(
        headers={},
        status=200,
    )

    client.get('/')

    assert mock_urlopen.call_args == mock.call(
        'GET', 'http://0.0.0.0:8003',
        body=b'',
        decode_content=False,
        headers={
            'Cookie': '',
            'X-Forwarded-Host': 'testserver',
            'X-Signature': mock.ANY
        },
        preload_content=False,
        redirect=False,
        retries=None
    )


@pytest.mark.parametrize(
    'status_code', [400, 401, 402, 403, 500, 502]
)
@mock.patch('urllib3.poolmanager.PoolManager.urlopen')
def test_response_codes(mock_urlopen, client, settings, status_code):
    mock_urlopen.return_value = urllib3.response.HTTPResponse(
        status=status_code,
    )

    response = client.get('/')

    assert response.status_code == status_code


@pytest.mark.parametrize('status_code', [200, 201, 301, 302])
@mock.patch('urllib3.poolmanager.PoolManager.urlopen')
def test_ok_response(mock_urlopen, client, settings, status_code):
    mock_urlopen.return_value = urllib3.response.HTTPResponse(
        body=json.dumps({'key': 'value'}),
        headers={'Content-Type': 'application/json',
                 'Content-Length': '2'},
        status=status_code,
    )

    response = client.get('/')

    assert response.status_code == status_code
    assert response.json() == {'key': 'value'}
