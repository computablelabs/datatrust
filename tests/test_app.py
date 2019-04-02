"""
Tests for app.py
"""

import pytest
import app

@pytest.fixture
def client():
    """
    Flask client for testing
    """
    app.app.config['TESTING'] = True
    client = app.app.test_client()
    yield client

def test_health(client):
    """
    Test that the /health endpoint returns OK
    """
    rv = client.get('/health')
    assert b'OK' in rv.data

def test_listing(client):
    """
    Test that the /listing endpoint returns OK for HTTP POST
    """
    rv = client.post('/listing')
    assert b'OK' in rv.data
