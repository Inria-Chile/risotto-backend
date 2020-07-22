def test_get_topics(client):
    response = client.get("/topics/")
    contents = response.get_json()

    assert contents["status"] == "OK"
    assert type(contents["payload"]) is list
    assert response.status_code == 200
