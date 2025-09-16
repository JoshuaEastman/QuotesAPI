import pytest
from django.urls import reverse
from model_bakery import baker
from quotes.models import Quote

pytestmark = pytest.mark.django_db

URL_NAME = 'quotes:quotes-random'

def test_random_without_tag_return_200_and_payload_shape(api_client):
    # Arrange
    baker.make(Quote, text='Stay hungry', author='Steve Jobs', tag='inspirational')

    # Act
    url = reverse(URL_NAME)
    resp = api_client.get(url)

    # Assert
    assert resp.status_code == 200
    body = resp.json()
    assert set(body.keys()) == {'type', 'count', 'results'}
    assert body['type'] == 'any'
    assert body['count'] == 1
    assert isinstance(body['results'], list) and len(body['results']) == 1

    item = body['results'][0]
    for key in ('id', 'text', 'author', 'tag'):
        assert key in item

def test_random_with_tag_filters_pool_and_marks_type(api_client):
    # Arrange: two tags present
    baker.make(Quote, text='T1', author='A1', tag='inspirational')
    baker.make(Quote, text='T2', author='A2', tag='humor')

    # Act
    url = reverse(URL_NAME)
    resp = api_client.get(url, {'tag': 'inspirational'})

    # Assert
    assert resp.status_code == 200
    body = resp.json()
    assert body['type'] == 'inspirational'
    assert body['count'] == 1
    assert len(body['results']) == 1
    assert body ['results'][0]['tag'].lower() == 'inspirational'

def test_unknown_tag_returns_404_with_spec_detail(api_client):
    # Arrange: DB has quotes, but not for queried tag
    baker.make(Quote, text='T1', author='A1', tag='inspirational')

    # Act
    url = reverse(URL_NAME)
    resp = api_client.get(url, {'tag': 'nope123'})

    # Assert
    assert resp.status_code == 404
    assert resp.json() == {'detail': "No quote found for tag 'nope123'."}

def test_random_empty_db_returns_404(api_client):
    # Arrange: Not necessary; testing empty db
    # Act
    url = reverse(URL_NAME)
    resp = api_client.get(url)
    assert resp.status_code == 404
    assert resp.json() == {'detail': 'No quotes available.'}

def test_random_tag_filter_is_case_insensitive(api_client):
    # Arrange
    baker.make(Quote, tag='inspirational', text='T1', author='A1')

    # Act
    url = reverse(URL_NAME)
    resp = api_client.get(url, {'tag': 'InSpIratIONal'})

    # Assert
    assert resp.status_code == 200
    body = resp.json()
    assert body['type'] == 'InSpIratIONal'
    assert body['results'][0]['tag'].lower() == 'inspirational'