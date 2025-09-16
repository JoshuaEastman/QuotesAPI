from django.urls import reverse

def test_demo_route_render(client):
    url = reverse('quotes:quotes-demo')
    res = client.get(url)
    assert res.status_code == 200
    assert b"Quotes API Demo" in res.content