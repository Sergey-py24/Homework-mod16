from fastapi import FastAPI, Path
from typing import Annotated


app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get('/users')
async def get_users():
    return users

@app.post('/user/{username}/{age}')
async def post_user(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username",
        example="Bobby")], age: Annotated[int, Path(ge=18, le=120, description="Enter age", example=55)]):
    current_index = str(int(max(users, key=int)) + 1)
    user = f"Имя: {username}, возраст: {age}"
    users[current_index] = user
    return f'The user {current_index} is registered'

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username",
        example="Bobby")],age: Annotated[int, Path(ge=18, le=120, description="Enter age", example=55)],
        user_id: Annotated[int, Path(ge=1)]):
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User with ID {user_id} is updated"

@app.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[int, Path(ge=1, description="Enter user_id")]):
     users.pop(str(user_id))
     return f"User with ID {user_id} has been deleted."
