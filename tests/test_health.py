import pytest
from app.main import App

@pytest.fixture()
def app():
    app = App().create_app()
    app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


def test_request_example(client):
    response = client.get("/hello")
    assert b"<p>hello, world</p>" in response.data