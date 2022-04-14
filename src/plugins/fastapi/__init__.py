from nonebot import get_app
from fastapi import FastAPI, Body
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from urllib.parse import parse_qsl
import base64, re

from .diy_bot import safe_send, re_send
from .db_io import (
    db_init,
    save_que,
    get_que,
    get_ans,
    update_que,
    update_ans,
    get_gid,
    get_num,
)


app: FastAPI = get_app()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


db_init()


@app.post("/send_question")
async def send_question(quest: str = Body(...)):
    base64_question = parse_qsl(quest)
    origin_question = base64.b64decode(base64_question[0][1]).decode("utf8")
    question = re.sub("'", "''", origin_question)
    result = await safe_send(question)
    save_que(str(result["message_id"]), question)
    return question


@app.post("/reask_question")
async def reask_question(quest: str = Body(...)):
    re_question = parse_qsl(quest)
    result = await re_send(re_question[0][1], re_question[2][1], re_question[1][1])
    question = re.sub("'", "''", re_question[2][1])
    g_id = get_gid(re_question[0][1])
    save_que(str(result["message_id"]), question, g_id)


@app.get("/get_question")
async def get_question():
    data_list = get_que()
    dict_array = []
    for i in range(0, len(data_list)):
        data_dict = {}
        data_dict["QUE_ID"] = data_list[i][0]
        data_dict["QUE_TXT"] = data_list[i][1]
        data_dict["ADOPT_ANS"] = data_list[i][2]
        data_dict["G_ID"] = data_list[i][3]
        dict_array.append(data_dict)
    return jsonable_encoder(dict_array)


@app.get("/get_answer/{que_id}")
async def get_answer(que_id: str):
    data_list = get_ans(que_id)
    dict_array = []
    for i in range(0, len(data_list)):
        data_dict = {}
        data_dict["ANS_ID"] = data_list[i][0]
        data_dict["QQ_NUM"] = data_list[i][1]
        data_dict["ANS_TXT"] = data_list[i][2]
        # data_dict["QUES_ID"] = data_list[i][3]
        data_dict["IS_ADOPT"] = data_list[i][4]
        dict_array.append(data_dict)
    return jsonable_encoder(dict_array)


@app.put("/update_question/{que_id}/{ans_id}")
async def update_question(que_id: str, ans_id: str):
    result = update_que(que_id, ans_id)
    return result


@app.put("/update_answer/{ans_id}/{is_adopt}")
async def update_question(ans_id: str, is_adopt: str):
    result = update_ans(
        is_adopt,
        ans_id,
    )
    return result


@app.get("/get_count/{count_item}")
async def get_answer(count_item: str):
    result = get_num(count_item)
    return result


# @app.get("/get_recent_quest")
# async def get_recent_quest():
#     data_list = get_rec_que("./msg/question.db")
#     return data_list
