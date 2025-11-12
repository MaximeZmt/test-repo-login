from ..model.user import User

import hashlib


def execute(memory, email, password):
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    u: User = memory.get(email)
    if u.password != password_hash:
        print("Error Login")
        return "failure", False
    else:
        print("Login - "+u.first_name+" "+u.last_name)
    return "success", True
