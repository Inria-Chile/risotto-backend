def test_get_papers(client):
    response = client.get("/papers/")
    contents = response.get_json()

    assert contents["status"] == "OK"
    assert type(contents["payload"]) is list
    assert type(contents["num_pages"]) is int
    assert type(contents["page"]) is int
    assert response.status_code == 200
