def test_get_topics(client):
    response = client.get("/topics/")
    contents = response.get_json()

    assert contents["status"] == "OK"
    assert type(contents["payload"]) is dict
    assert type(contents["payload"]["topics"]) is list
    assert type(contents["payload"]["subtopics"]) is dict
    assert response.status_code == 200
