import pytest
from api.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_new_comment(client):
    response = client.post('/api/comment/new', json={
        'email': 'alice@example.com',
        'comment': 'first post!',
        'content_id': 1
    })
    assert response.status_code == 200
    assert response.get_json() == {'status': 'SUCCESS', 'message': 'comment created and associated with content_id 1'}

def test_list_comments(client):
    client.post('/api/comment/new', json={
        'email': 'alice@example.com',
        'comment': 'first post!',
        'content_id': 1
    })
    client.post('/api/comment/new', json={
        'email': 'bob@example.com',
        'comment': 'I agree',
        'content_id': 1
    })
    response = client.get('/api/comment/list/1')
    assert response.status_code == 200
    comments = response.get_json()
    assert len(comments) == 2
    assert comments[0]['email'] == 'alice@example.com'
    assert comments[1]['email'] == 'bob@example.com'
