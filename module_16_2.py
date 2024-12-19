from fastapi import FastAPI, Path
from typing import Annotated


app = FastAPI()

@app.get('/')
async def welcome():
    return 'Главная страница'

@app.get('/user/admin')
async def get_admin():
    return 'Вы вошли как администратор'

@app.get('/user/{user_id}')
async def get_user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='11')]):
    return  f'Вы вошли как пользователь № {user_id}'

@app.get('/user/{user_name}/{age}')
async def info(user_name: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='Bob')]
               , age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='99')]):
    return  f'Информация о пользователе.Имя: {user_name}, Возраст: {age}'

