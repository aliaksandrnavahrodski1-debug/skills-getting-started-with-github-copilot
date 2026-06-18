from src.app import activities


def test_get_activities(client):
    resp = client.get("/activities")
    assert resp.status_code == 200
    data = resp.json()
    # response should match in-memory activities
    assert isinstance(data, dict)
    assert len(data) == len(activities)
    assert "Chess Club" in data


def test_signup_and_remove_participant(client):
    activity = "Chess Club"
    email = "tester@example.com"

    # signup
    resp = client.post(f"/activities/{activity}/signup", params={"email": email})
    assert resp.status_code == 200
    assert email in activities[activity]["participants"]

    # remove
    resp = client.delete(f"/activities/{activity}/participant", params={"email": email})
    assert resp.status_code == 200
    assert email not in activities[activity]["participants"]


def test_signup_unknown_activity_returns_404(client):
    resp = client.post("/activities/NoSuchActivity/signup", params={"email": "x@example.com"})
    assert resp.status_code == 404


def test_remove_nonexistent_participant_returns_404(client):
    activity = "Programming Class"
    resp = client.delete(f"/activities/{activity}/participant", params={"email": "notfound@example.com"})
    assert resp.status_code == 404
