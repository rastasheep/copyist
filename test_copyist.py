import pytest
import os
import copyist
from flask import json

@pytest.fixture
def client(request):
    copyist.app.config['TESTING'] = True
    client = copyist.app.test_client()

    return client

def test_v1_without_url_param(client):
    resp = client.get('/v1')
    data = json.loads(resp.data)

    assert resp.status_code == 404
    assert data == {'message': 'Page not found.'}

def test_404_page(client):
    resp = client.get('/404')
    data = json.loads(resp.data)

    assert resp.status_code == 404
    assert data == {'message': 'Page not found.'}
