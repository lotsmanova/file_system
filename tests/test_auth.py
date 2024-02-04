jwt_token = None


def auth_header():
    global jwt_token
    return {"Authorization": f"Bearer {jwt_token}"}


def test_register(test_client):

    # TestCase1 register user
    response = test_client.post('/register', json={'username': 'testuser', 'password': 'testpass'})
    data = response.get_json()
    assert response.status_code == 200
    assert 'access_token' in data


def test_login(test_client):
    global jwt_token
    # TestCase2 login user
    response = test_client.post('/login', json={'username': 'testuser', 'password': 'testpass'})
    data = response.get_json()

    jwt_token = data['access_token']

    assert response.status_code == 200
    assert 'access_token' in data
