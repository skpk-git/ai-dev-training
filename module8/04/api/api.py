from fastapi import FastAPI
from pydantic import BaseModel

from database.database import (
    initialize_database,
    add_user,
    get_users,
    get_user_by_id
)


app = FastAPI(
    title="User Database API"
)


initialize_database()


class UserRequest(BaseModel):
    name: str
    phone: str
    user_key: str


@app.get("/users")
def api_get_users():

    return get_users()


@app.get("/users/{user_id}")
def api_get_user(user_id: int):

    user = get_user_by_id(user_id)

    if user is None:
        return {
            "success": False,
            "message": "User not found"
        }

    return user


@app.post("/users")
def api_add_user(user: UserRequest):

    return add_user(
        user.name,
        user.phone,
        user.user_key
    )