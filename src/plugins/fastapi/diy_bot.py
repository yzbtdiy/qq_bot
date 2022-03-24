from nonebot.adapters.onebot.v11 import MessageSegment, GroupMessageEvent
from nonebot.adapters.onebot.v11.exception import ActionFailed, NetworkError
from nonebot import get_bots, on_message
from nonebot.log import logger

import re

from .db_io import save_ans


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


reply = on_message(priority=100)


@reply.handle()  # 调用装饰器
async def rec_group_msg(group_msg_event: GroupMessageEvent):  # 创建事件处理函数
    origin_msg = group_msg_event.get_plaintext().strip()  # 获取群内消息
    group_msg = re.sub("'", "''", origin_msg)
    sender_qq = group_msg_event.user_id
    reply_msg = str(group_msg_event.raw_message)  # 获取row_message
    reply_msg_id = re.findall(r"id=(.+?)]", reply_msg)
    sender_msg_id = group_msg_event.message_id
    replay_user_id = re.findall(
        r"qq=(.+?)]", reply_msg
    )  # 根据row_message中是否包含 reply id= 判断是否回复特定消息

    if (
        reply_msg_id and replay_user_id[0] == "320785209"
    ):  # 根据row_message中是否包含 at qq= 判断是否回复特定消息
        save_ans(
            "./msg/" + "answer.db", sender_msg_id, sender_qq, group_msg, reply_msg_id[0]
        )
    # else:
    #     save_answer_to_db("./msg/" + "savemsg.db", "null", sender_id, group_msg)

    # if group_msg == "/问题":  # 根据消息内容，判断回复什么
    #     await reply.finish("question1, question2, question3")  # 发送消息，并结束该事件
    # elif group_msg == "/help":
    #     await reply.finish('Please send "问题" to me')
    # else:
    #     await reply.finish()
