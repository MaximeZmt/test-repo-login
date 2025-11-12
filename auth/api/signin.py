from ..model.user import User

import hashlib


def execute(memory, email, firstname, lastname, password):
    if memory.exist(email):
        return "fail", False

    password_hash = hashlib.sha256(password.encode()).hexdigest()
    u = User(email, firstname, lastname, password_hash)
    memory.put(email, u)
    return "success", True
