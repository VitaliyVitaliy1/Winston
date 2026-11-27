def test_get_post_by_id(api):
    """GET /posts/1 — должен вернуть пост с id=1."""
    response = api.get(f"{api.base_url}/posts/1")

    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "title" in data
    assert "body" in data
    assert isinstance(data["title"], str)


def test_get_all_posts(api):
    """GET /posts — должен вернуть 100 постов."""
    response = api.get(f"{api.base_url}/posts")

    assert response.status_code == 200
    posts = response.json()
    assert isinstance(posts, list)
    assert len(posts) == 100


def test_create_post(api):
    """POST /posts — должен создать пост и вернуть его с id."""
    payload = {
        "title": "autotest",
        "body": "created by pytest",
        "userId": 1,
    }
    response = api.post(f"{api.base_url}/posts", json=payload)

    assert response.status_code == 201
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert "id" in data


def test_update_post(api):
    """PUT /posts/1 — должен обновить пост."""
    payload = {"id": 1, "title": "updated title", "body": "new body", "userId": 1}
    response = api.put(f"{api.base_url}/posts/1", json=payload)

    assert response.status_code == 200
    assert response.json()["title"] == "updated title"


def test_delete_post(api):
    """DELETE /posts/1 — должен вернуть 200."""
    response = api.delete(f"{api.base_url}/posts/1")
    assert response.status_code == 200


def test_get_nonexistent_post(api):
    """GET /posts/9999 — должен вернуть 404."""
    response = api.get(f"{api.base_url}/posts/9999")
    assert response.status_code == 404
