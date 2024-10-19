import random

from werkzeug.security import generate_password_hash

from tp1_gl5_devops.models.user import User

USERS = []


def createUser(email: str, password: str, firstname: str, lastname: str) -> User:
    new_acc = User(
        id=random.randint(0, 9000),
        firstName=firstname,
        lastName=lastname,
        email=email,
        password=generate_password_hash(password, 'sha256'),
    )
    USERS.append(new_acc)
    return new_acc


def findOneByEmail(email: str) -> User | None:
    try:
        return next(u for u in USERS if u.email == email)
    except Exception:
        return None


def findOne(id: int) -> User | None:
    try:
        return next(u for u in USERS if u.id == id)
    except Exception:
        return None


def findAll() -> list[User]:
    try:
        return USERS
    except Exception:
        return []


def userToJSON(user: User) -> dict:
    return {
        'id': user.id,
        'email': user.email,
        'password': user.password,
        'firstname': user.firstName,
        'lastname': user.lastName,
    }
