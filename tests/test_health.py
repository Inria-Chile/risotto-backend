def test_get_health(client):
    response = client.get("/health")
    assert response.data.decode() == "OK"
    assert response.status_code == 200


def test_get_not_found(client):
    response = client.get("/health-404-not-found")
    assert response.status_code == 404
