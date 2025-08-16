import pytest
from app import app as flask_app

@pytest.fixture
def app():
    flask_app.config.update({
        "TESTING": True,
    })
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_index_logged_out(client):
    res = client.get('/')
    assert res.status_code == 200
    assert b"<h2>Login</h2>" in res.data

def test_login_success(client):
    res = client.post('/login', data={
        "username": "admin",
        "password": "password"
    }, follow_redirects=True)
    assert res.status_code == 200
    assert b"<h1>Hello, admin!</h1>" in res.data

def test_login_failure(client):
    res = client.post('/login', data={
        "username": "wrong",
        "password": "user"
    }, follow_redirects=True)
    assert res.status_code == 200
    assert b"<p style=\"color: red;\">Invalid credentials</p>" in res.data

def test_logout(client):
    # First, log in
    client.post('/login', data={
        "username": "admin",
        "password": "password"
    }, follow_redirects=True)

    # Then, log out
    res = client.get('/logout', follow_redirects=True)
    assert res.status_code == 200
    assert b"<h2>Login</h2>" in res.data

def test_index_logged_in(client):
    with client.session_transaction() as session:
        session['username'] = 'testuser'
    res = client.get('/')
    assert res.status_code == 200
    assert b"<h1>Hello, testuser!</h1>" in res.data