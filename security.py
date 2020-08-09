from secrets import compare_digest
from user import User

users = [
    User(1, "kasia", "Test123!@#")
]

username_mapping = {u.username: u for u in users}

userid_mapping = {u.id: u for u in users}


def authenticate(username, password):
    user = userid_mapping.get(username, None)
    if user and compare_digest(user.password, password):
        return user


def identity(payload):
    user_id = payload["identity"]
    return userid_mapping.get(user_id, None)
