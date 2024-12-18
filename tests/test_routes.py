import json


def test_create_todo(client, todo_data):
    response = client.post('/todos',
                           data=json.dumps(todo_data),
                           content_type='application/json'
                           )

    assert response.status_code == 201

    data = json.loads(response.data)
    assert data['title'] == todo_data['title']
    assert data['description'] == todo_data['description']
    assert data['completed'] == todo_data['completed']


def test_get_todos(client, todo_data):
    for i in range(3):
        todo_data['title'] = f'Test Todo {i + 1}'
        client.post('/todos',
                    data=json.dumps(todo_data),
                    content_type='application/json'
                    )

    response = client.get('/todos')

    assert response.status_code == 200

    data = json.loads(response.data)
    assert len(data) == 3


def test_update_todo(client, todo_data):
    response = client.post('/todos',
                           data=json.dumps(todo_data),
                           content_type='application/json'
                           )
    todo_id = json.loads(response.data)['id']

    update_data = {
        'title': 'Updated Todo',
        'completed': True
    }

    response = client.put(f'/todos/{todo_id}',
                          data=json.dumps(update_data),
                          content_type='application/json'
                          )

    assert response.status_code == 200

    data = json.loads(response.data)
    assert data['title'] == 'Updated Todo'
    assert data['completed'] is True


def test_delete_todo(client, todo_data):
    response = client.post('/todos',
                           data=json.dumps(todo_data),
                           content_type='application/json'
                           )
    todo_id = json.loads(response.data)['id']

    response = client.delete(f'/todos/{todo_id}')

    assert response.status_code == 204

    response = client.get('/todos')
    data = json.loads(response.data)
    assert len(data) == 0


def test_create_invalid_todo(client):
    invalid_todo = {
        'description': 'Invalid Todo'
    }

    response = client.post('/todos',
                           data=json.dumps(invalid_todo),
                           content_type='application/json'
                           )

    assert response.status_code == 400
