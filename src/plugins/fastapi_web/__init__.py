from nonebot import get_app
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
import sqlite3, datetime

app: FastAPI = get_app()


def get_answer_from_db(db_file_name, tab_name):  # 从数据库中获取答案
    get_data_sql = "SELECT QUES_ID, QQ_NUM, USER_CON FROM '%s'" % (tab_name)
    db_con = sqlite3.connect(db_file_name)
    db_cursor = db_con.cursor()
    db_cursor.execute(get_data_sql)
    data = db_cursor.fetchall()
    return data


def get_quest_from_db(db_file_name, tab_name):  # 从数据库中获取答案
    get_data_sql = "SELECT QUES_ID, QUES_TXT FROM '%s'" % (tab_name)
    db_con = sqlite3.connect(db_file_name)
    db_cursor = db_con.cursor()
    db_cursor.execute(get_data_sql)
    data = db_cursor.fetchall()
    return data


@app.get("/get_answer")
async def get_answer():
    tab_name = "ans_" + str(datetime.date.today().__format__("%Y%m%d"))
    data_list = get_answer_from_db("./msg/answer.db", tab_name)
    dict_array = []
    for i in range(0, len(data_list)):
        if i <= len(data_list):
            data_dict = {}
            data_dict["QUES_ID"] = data_list[i][0]
            data_dict["QQ_NUM"] = data_list[i][1]
            data_dict["USER_CON"] = data_list[i][2]
            dict_array.append(data_dict)
    return jsonable_encoder(dict_array)


@app.get("/get_question")
async def get_question():
    tab_name = "que_" + str(datetime.date.today().__format__("%Y%m%d"))
    data_list = get_quest_from_db("./msg/question.db", tab_name)
    dict_array = []
    for i in range(0, len(data_list)):
        if i <= len(data_list):
            data_dict = {}
            data_dict["QUES_ID"] = data_list[i][0]
            data_dict["QUES_TXT"] = data_list[i][1]
            dict_array.append(data_dict)
    return jsonable_encoder(dict_array)
