from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_read_example():
    response = client.get("/example")
    assert response.status_code == 200
    assert response.json() == {"message": "This is an example endpoint"}


def test_root():
    # Make the request without following redirects using the updated argument `follow_redirects`
    response = client.get("/", follow_redirects=False)

    # Check for the redirect status code (307 for temporary, 301 for permanent)
    assert response.status_code == 307

    # Check if the location header points to /example
    assert response.headers["location"] == "/example"

    # Optionally, follow the redirect and test the /example endpoint separately
    response = client.get("/example")
    assert response.status_code == 200
    assert response.json() == {"message": "This is an example endpoint"}
