from app.models import Todo
from app import db

def test_todo_model(app):
    with app.app_context():
        # Criar uma tarefa
        todo = Todo(
            title='Test Todo',
            description='Test Description',
            completed=False
        )
        db.session.add(todo)
        db.session.commit()

        # Verificar criação
        assert todo.id is not None
        assert todo.title == 'Test Todo'
        assert todo.description == 'Test Description'
        assert todo.completed is False

        # Testar método to_dict
        todo_dict = todo.to_dict()
        assert todo_dict['title'] == 'Test Todo'
        assert 'id' in todo_dict
        assert 'created_at' in todo_dict