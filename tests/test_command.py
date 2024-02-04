from tests.test_auth import auth_header


def test_hello(test_client):
    # TestCase1 hello user
    response = test_client.get('/', headers=auth_header())
    assert response.status_code == 200


def test_create_file(test_client):
    # TestCase2 create file
    response = test_client.post('/touch', json={"file_name": "test.txt", "path": "/home/v", "text": "test"},
                                headers=auth_header())
    data = response.get_json()
    assert response.status_code == 200
    assert 'message' in data


def test_create_directory(test_client):
    # TestCase3 create directory
    response = test_client.post('/mkdir', json={"dir_name": "test_dir", "path": "/home/v"}, headers=auth_header())
    data = response.get_json()
    assert response.status_code == 200
    assert 'message' in data


def test_chmod(test_client):
    # TestCase4 change mod
    response = test_client.post('/chmod', json={"object_name": "/home/v/test.txt", "mask": 777}, headers=auth_header())
    data = response.get_json()
    assert response.status_code == 200
    assert 'message' in data


def test_chown(test_client):
    # TesCase5 change owner
    response = test_client.post('/chown', json={"object_name": "/home/v/test_dir", "owner": "v"}, headers=auth_header())
    data = response.get_json()
    assert response.status_code == 200
    assert 'message' in data


def test_delete(test_client):
    # TestCase6 delete file or directory
    response = test_client.delete('/rm', json={"object_name": "/home/v/test_dir"}, headers=auth_header())
    data = response.get_json()
    assert response.status_code == 200
    assert 'message' in data


def test_list_dir(test_client):
    # TestCase7 list file directory
    response = test_client.get('/ls', json={"object_name": "/home/v"}, headers=auth_header())
    data = response.get_json()
    assert response.status_code == 200
    assert 'list_directory' in data