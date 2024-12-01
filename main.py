from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"message": "Главная страница"}

@app.get("/user/admin")
async def welcome_a() -> dict:
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def welcome_id(user_id: str) -> dict:
    return {"message": f"Вы вошли как пользователь {user_id}"}

@app.get("/user/{username}/{age}")
async def welcome_info(username: str, age: int) -> dict:
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8001)