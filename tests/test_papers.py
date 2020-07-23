def test_get_papers(client):
    response = client.get("/papers/")
    contents = response.get_json()

    assert contents["status"] == "OK"
    assert type(contents["payload"]) is dict
    assert type(contents["payload"]["papers"]) is list
    assert type(contents["payload"]["num_results"]) is int
    assert type(contents["payload"]["num_pages"]) is int
    assert type(contents["payload"]["page"]) is int
    assert response.status_code == 200
