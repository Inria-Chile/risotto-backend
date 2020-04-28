def test_get_health(client):
    response = client.get("/health")
    assert response.data.decode() == "OK"
    assert response.status_code == 200
