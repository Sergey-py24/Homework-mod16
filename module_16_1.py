from fastapi import FastAPI


app = FastAPI()

@app.get('/')
async def welcome():
    return {'message': 'Главная страница'}

@app.get('/user/admin')
async def get_admin():
    return {'message': 'Вы вошли как администратор'}

@app.get('/user/{user_id}')
async def get_user(user_id):
    return {'message': f'Вы вошли как пользователь № {user_id}'}

@app.get('/user')
async def info(user_name, age):
    return {'message': f'Информация о пользователе.Имя: {user_name}, Возраст: {age}'}
