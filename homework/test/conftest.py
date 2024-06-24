import pytest
from openapi_client import ApiClient, Configuration
from openapi_client.api import DefaultApi


@pytest.fixture(scope="module")
def api_client():
    config = Configuration(host="http://localhost:8000")
    with ApiClient(configuration=config) as api_client:
        yield api_client


@pytest.fixture(scope="module")
def default_api(api_client):
    return DefaultApi(api_client)
