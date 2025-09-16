import pytest
from django.urls import reverse
from model_bakery import baker
from quotes.models import Quote

pytestmark = pytest.mark.django_db

def test_health_ok(api_client):
    resp = api_client.get(reverse('quotes:quotes-health'))
    assert resp.status_code == 200
    assert resp.json() == {'status': 'ok'}