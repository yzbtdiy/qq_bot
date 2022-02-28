from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
import sqlite3

from starlette.middleware.gzip import GZipMiddleware
from starlette.middleware.cors import CORSMiddleware
import uvicorn


app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


def get_data_from_db(db_file_name, tab_name):  # 从数据库中获取答案
    get_data_sql = "SELECT QUES_ID, QQ_NUM, USER_CON FROM '%s'" % (tab_name)
    db_con = sqlite3.connect(db_file_name)
    db_cursor = db_con.cursor()
    db_cursor.execute(get_data_sql)
    data = db_cursor.fetchall()
    return data


# @app.middleware("http")
# async def add_CORS_header(request: Request, call_next):
#     response = await call_next(request)
#     response.headers["Access-Control-Allow-Origin"] = "*"
#     response.headers["Access-Control-Allow-Methods"] = "*"
#     response.headers["Access-Control-Allow-Headers"] = "*"
#     return response


@app.get("/get_answer")
async def get_answer():

    # if requests.method == "GET":
    data = get_data_from_db("../msg/answer.db", "ans_20220220")
    return jsonable_encoder(data)


if __name__ == "__main__":
    uvicorn.run(app=app, host="127.0.0.1", port=5000, log_level="info")