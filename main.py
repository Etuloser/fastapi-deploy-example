import uvicorn

from fastapi import FastAPI
from pydantic import BaseModel
from config.settings import settings

app = FastAPI()


class Resp(BaseModel):
    data: dict
    message: str
    code: int = 10020


@app.get("/", response_model=Resp)
def read_root() -> dict:
    return {
        "data": {},
        "message": f"endpoint is '/'",
        "code": 10020,
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=settings.PORT, log_level="info", reload=settings.DEBUG)
