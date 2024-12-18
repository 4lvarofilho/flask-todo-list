import os
import pytest
from dotenv import load_dotenv
from app import create_app, db
from app.models import Todo

load_dotenv()


@pytest.fixture(scope='session')
def app():
    app = create_app()

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['TESTING'] = True

    with app.app_context():
        db.create_all()
        yield app

        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture(autouse=True)
def clear_database(app):
    with app.app_context():
        for table in reversed(db.metadata.sorted_tables):
            db.session.execute(table.delete())
        db.session.commit()


@pytest.fixture
def todo_data():
    return {
        'title': 'Test Todo',
        'description': 'Test Description',
        'completed': False
    }