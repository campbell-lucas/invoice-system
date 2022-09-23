from django.urls import reverse


def test_view_home(client):
    url = reverse('home:landing')
    response = client.get(url)

    assert response.status_code == 302
