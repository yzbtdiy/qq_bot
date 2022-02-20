from nonebot import get_app
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
import sqlite3


app: FastAPI = get_app()


def get_data_from_db(db_file_name, tab_name):  # 从数据库中获取答案
    get_data_sql = "SELECT QUES_ID, QQ_NUM, USER_CON FROM '%s'" % (tab_name)
    db_con = sqlite3.connect(db_file_name)
    db_cursor = db_con.cursor()
    db_cursor.execute(get_data_sql)
    data = db_cursor.fetchall()
    return data


@app.get("/get_answer")
async def get_answer():

    # if requests.method == "GET":
    data = get_data_from_db("./msg/answer.db", 'ans_20220220')
    return jsonable_encoder(data)
