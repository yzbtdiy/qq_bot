from ast import Str
from nonebot.log import logger
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot.adapters.onebot.v11.exception import ActionFailed, NetworkError
from nonebot import require, get_bots, get_app

import sqlite3, datetime

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
import sqlite3
from typing import Optional
from pydantic import BaseModel

app: FastAPI = get_app()


scheduler = require("nonebot_plugin_apscheduler")
assert scheduler is not None
scheduler = scheduler.scheduler


def save_question(file_name, question_id, question_txt):  # 保存问题到数据库
    tab_name = "ans" + str(datetime.date.today().__format__("%Y%m%d"))
    create_tab = (
        "CREATE TABLE IF NOT EXISTS '%s'(ID INTEGER PRIMARY KEY AUTOINCREMENT, QUES_ID text, QUES_TXT text)"
        % (tab_name)
    )
    add_data = "INSERT INTO '%s'(ID, QUES_ID, QUES_TXT) VALUES (NULL, '%s', '%s')" % (
        tab_name,
        question_id,
        question_txt,
    )
    with sqlite3.connect(file_name) as db_con:
        db_con.execute(create_tab)
        db_con.execute(add_data)


async def safe_send(bot_id, send_type, type_id, message, at=False):
    """发送出现错误时, 尝试重新发送, 并捕获异常且不会中断运行"""

    try:
        bot = get_bots()[str(bot_id)]
    except KeyError:
        logger.error(f"推送失败，Bot（{bot_id}）未连接")
        return

    if at and (await bot.get_group_at_all_remain(group_id=type_id))["can_at_all"]:
        message = MessageSegment.at("all") + message

    try:
        return await bot.call_api(
            "send_" + send_type + "_msg",
            **{
                "message": message,
                "user_id" if send_type == "private" else "group_id": type_id,
            },
        )
    except ActionFailed as e:
        url = "https://haruka-bot.sk415.icu/"
        logger.error(f"推送失败，账号可能被风控（{url}），错误信息：{e.info}")
    except NetworkError as e:
        logger.error(f"推送失败，请检查网络连接，错误信息：{e.msg}")


# @scheduler.scheduled_job("interval", seconds=10, id="dynamic_sched")
# async def save_db():
#     ques = "hello,world"
#     result = await safe_send(320785209, "group", 755048599, ques)
#     print(result)
#     save_question("./msg/question.db", str(result["message_id"]), ques)


class Item(BaseModel):
    id: Optional[int] = None
    question: str

@app.post("/send_question")
async def send_question(item: Item):
    ques =  item.question 
    result = await safe_send(320785209, "group", 755048599, ques)
    # print(result)
    save_question("./msg/question.db", str(result["message_id"]), ques)
