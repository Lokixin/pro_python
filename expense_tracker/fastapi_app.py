from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse

from expense_tracker.fake_db import user_list
from expense_tracker.models import UserIn, UserNotFound

app = FastAPI()


@app.get("/healthcheck/")
async def healthcheck() -> dict:
    return {"message": "ok"}


@app.get("/users/", response_model=dict[int, UserIn])
async def users():
    return user_list


@app.get(
    "/users/{key}/",
    response_model=UserIn | dict,
    responses={404: {"model": UserNotFound}},
)
async def user_by_key(key: int = 0, params: list[str] | None = Query(default=None)):
    try:
        if params:
            return {key: user_list[key].get(param) for param in params}
        return user_list[key]
    except KeyError:
        return JSONResponse(
            content={"message": "Error: User Not Found", "detail": key},
            status_code=404,
        )


@app.post("/users/create/", response_model=UserIn)
async def create_user(user_in: UserIn) -> UserIn:
    user = UserIn(
        name=user_in.name,
        surname=user_in.surname,
        age=user_in.age,
        email=user_in.email,
    )
    new_key = max(user_list.keys()) + 1
    user_list[new_key] = user.dict()
    return user
