



from fastapi import FastAPI, Path, HTTPException
from typing import Annotated, List
from pydantic import BaseModel

app = FastAPI()

users = []

class User(BaseModel):
    id: int = None
    username: str
    age: int

@app.get('/')
async def welcome():
    return  'Главная страница'

@app.get("/users")
def get_users() -> List[User]:
    return users

@app.post("/user/{username}/{age}")
def post_user(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username')],
                    age: Annotated[int, Path(ge=18, le=120, description='Enter age')]) -> User:
    user_id = (users[-1].id + 1) if users else 1
    user = User(id=user_id, username=username, age=age)
    users.append(user)
    return user

@app.put("/user/{user_id}/{username}/{age}")
def update_user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID')],
                      username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username')],
                      age: Annotated[int, Path(ge=18, le=120, description='Enter age')]) -> User:
    try:
        for user in users:
            if user.id == user_id:
                user.username = username
                user.age = age
                return user
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')

@app.delete("/user/{user_id}")
def delete_user(user_id: Annotated[int, Path(ge=1, description="Enter user_id")]):
    try:
        users.pop(user_id - 1)
        return f"User with ID {user_id} has been deleted"
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")