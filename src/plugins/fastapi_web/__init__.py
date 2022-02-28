from nonebot import get_app
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
import sqlite3
from typing import Optional
from pydantic import BaseModel

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
    data_list = get_data_from_db("./msg/answer.db", "ans_20220220")
    data_dict = {}
    dict_array = []
    for i in data_list:
        data_dict["QUES_ID"] = i[0]
        data_dict["QQ_NUM"] = i[1]
        data_dict["USER_CON"] = i[2]
        dict_array.append(data_dict)
    return jsonable_encoder(dict_array)






# @app.post("/push_question")
# async def push_question(request: Request, question: str = Form(...)):
#     print("question", question)


# matcher = on_message()
# @matcher.handle()
# async def save_question():
