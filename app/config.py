import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "postgresql://todo_user:todo_pass@db:5432/todo_db",
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False