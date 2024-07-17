from app import app
from app.models import *


def mock_data():
    ...

    db.session.add_all([])
    db.session.commit()
    print("mock data added")


with app.app_context():
    db.create_all()

    print("database created")
    mock_data()
