"""
Tests for app.py
All API endpoint tests live here
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
    Test that the /health endpoint returns OK for HTTP GET
    """
    rv = client.get('/health')
    assert b'OK' in rv.data

def test_get_listing(client):
    """
    Test the HTTP GET request to the listing endpoint
    """
    rv = client.get('/api/v1/listing', json='')
    assert b'No input data provided' in rv.data

def test_listing_empty_body(client):
    """
    Test that a POST to the listing endpoint with no data returns an error
    """
    rv = client.post('/api/v1/listing', json='')
    assert b'No input data provided' in rv.data
