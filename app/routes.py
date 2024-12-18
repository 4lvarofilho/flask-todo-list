from flask import jsonify, request, abort
from app import db
from app.models import Todo
from app.schemas import TodoSchema
from marshmallow import ValidationError

todo_schema = TodoSchema()
todos_schema = TodoSchema(many=True)


def init_routes(app):
    @app.route('/todos', methods=['GET'])
    def get_todos():
        todos = Todo.query.order_by(Todo.created_at.desc()).all()
        return jsonify(todos_schema.dump(todos))

    @app.route('/todos', methods=['POST'])
    def create_todo():
        try:
            data = todo_schema.load(request.json)
        except ValidationError as err:
            return jsonify(err.messages), 400

        todo = Todo(
            title=data['title'],
            description=data.get('description'),
            completed=data.get('completed', False)
        )
        db.session.add(todo)
        db.session.commit()
        return jsonify(todo_schema.dump(todo)), 201

    @app.route('/todos/<int:todo_id>', methods=['PUT'])
    def update_todo(todo_id):
        todo = Todo.query.get_or_404(todo_id)

        try:
            data = todo_schema.load(request.json, partial=True)
        except ValidationError as err:
            return jsonify(err.messages), 400

        if 'title' in data:
            todo.title = data['title']
        if 'description' in data:
            todo.description = data['description']
        if 'completed' in data:
            todo.completed = data['completed']

        db.session.commit()
        return jsonify(todo_schema.dump(todo))

    @app.route('/todos/<int:todo_id>', methods=['DELETE'])
    def delete_todo(todo_id):
        todo = Todo.query.get_or_404(todo_id)
        db.session.delete(todo)
        db.session.commit()
        return '', 204