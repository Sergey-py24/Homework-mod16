

from fastapi import FastAPI, Path, HTTPException, Request
from typing import Annotated, List, Type
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True}, debug=True)
templates = Jinja2Templates(directory='templates')
users = []

class User(BaseModel):
    id: int = None
    username: str
    age: int

@app.get('/', response_model=List[User])
async def all_users(request: Request) -> HTMLResponse:
    return  templates.TemplateResponse("users.html",{"request": request, "users": users})

@app.get("/user/{user_id}", response_model=User)
def get_user(request: Request, user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID',
            example='1')]) -> HTMLResponse:
    for user in users:
        if user.id == user_id:
            return templates.TemplateResponse("users.html", {"request": request, "user": users[user_id-1]})
    raise HTTPException(status_code=404, detail="User was not found")

@app.post("/user/{username}/{age}")
def post_user(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username',
    example='Bobby')], age: Annotated[int, Path(ge=18, le=120, description='Enter age',
    example='20')]) -> User:
    user_id = (users[-1].id + 1) if users else 1
    user = User(id=user_id, username=username, age=age)
    users.append(user)
    return user

@app.put("/user/{user_id}/{username}/{age}")
def update_user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='1')],
     username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username',
     example='Bobby')],age: Annotated[int, Path(ge=18, le=120, description='Enter age',
     example='33')]) -> User:
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail='User was not found')

@app.delete("/user/{user_id}")
def delete_user(user_id: Annotated[int, Path(ge=1, description="Enter user_id",
                example='2')]):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail="User was not found")



#  python -m uvicorn module_16_5:app --reload
