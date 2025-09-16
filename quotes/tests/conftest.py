import pytest
from django.core.cache import cache
from rest_framework.test import APIClient
from quotes.throttling import GlobalRateThrottle, IPRateThrottle

@pytest.fixture
def api_client():
    return APIClient()

# Auto clear Django cache
@pytest.fixture(autouse=True)
def _reset_throttle_cache():
    cache.clear()
    yield
    cache.clear()