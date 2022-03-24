from nonebot import get_app
from fastapi import FastAPI, Body
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from urllib.parse import parse_qsl
import base64, re

from .diy_bot import safe_send
from .db_io import (
    save_que,
    get_que,
    get_ans,
    update_que,
    update_ans,
)


app: FastAPI = get_app()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/send_question")
async def send_question(quest: str = Body(...)):
    base64_question = parse_qsl(quest)
    origin_question = base64.b64decode(base64_question[0][1]).decode("utf8")
    question = re.sub("'", "''", origin_question)
    result = await safe_send(320785209, "group", 755048599, question)
    save_que("./msg/question.db", str(result["message_id"]), question)
    return question


@app.get("/get_question")
async def get_question():
    data_list = get_que("./msg/question.db")
    dict_array = []
    for i in range(0, len(data_list)):
        data_dict = {}
        data_dict["QUES_ID"] = data_list[i][0]
        data_dict["QUES_TXT"] = data_list[i][1]
        data_dict["ADOPT_ANS"] = data_list[i][2]
        dict_array.append(data_dict)
    return jsonable_encoder(dict_array)


@app.get("/get_answer/{quest_id}")
async def get_answer(quest_id: str):
    data_list = get_ans("./msg/answer.db", quest_id)
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


@app.get("/update_question/{quest_id}/{answer_id}")
async def update_question(quest_id: str, answer_id: str):
    result = update_que("./msg/question.db", quest_id, answer_id)
    return result


@app.get("/update_answer/{answer_id}/{is_adopt}")
async def update_question(answer_id: str, is_adopt: str):
    result = update_ans(
        "./msg/answer.db",
        is_adopt,
        answer_id,
    )
    return result
