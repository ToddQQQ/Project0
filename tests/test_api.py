import requests
import pytest
import os

# API  URL
BASE_URL = os.getenv("API_BASE_URL", "http://127.0.0.1:8000")


@pytest.fixture(scope="session")
def api_url():
    """Fixture: API  URL"""
    return BASE_URL


def test_server_health(api_url):
    """test server health"""
    response = requests.get(f"{api_url}/docs")  # 
    assert response.status_code == 200, f"Server health check failed: {response.text}"


def test_generate_reply(api_url):
    """test generate_reply endpoint"""
    payload = {"text": "What do you think about AI?"}
    response = requests.post(f"{api_url}/generate_reply/", json=payload)

    assert response.status_code == 200, f"Unexpected response code: {response.status_code}"
    json_response = response.json()

    assert "reply" in json_response, "Response is missing 'reply' field"
    assert isinstance(json_response["reply"], str), "Reply field should be a string"


def test_invalid_input(api_url):
    """test invalid input to generate_reply endpoint"""
    payload = {"wrong_key": "This is an invalid request"}
    response = requests.post(f"{api_url}/generate_reply/", json=payload)

    assert response.status_code == 422, f"Expected 422 error, got {response.status_code}"


def test_cors_headers(api_url):
    """test CORS headers are present"""
    response = requests.options(f"{api_url}/generate_reply/")
    
    assert "access-control-allow-origin" in response.headers, "Missing CORS header"
