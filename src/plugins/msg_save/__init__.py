from nonebot.adapters.onebot.v11 import GroupMessageEvent
from nonebot.plugin import on_message
import re, sqlite3, datetime

reply = on_message(priority=100)  # 注册事件响应器，优先度很低


@reply.handle()  # 调用装饰器
async def rec_group_msg(group_msg_event: GroupMessageEvent):  # 创建事件处理函数
    group_msg = group_msg_event.get_plaintext().strip()  # 获取群内消息
    sender_id = group_msg_event.user_id
    # final_msg = str(sender_id) + ", " + group_msg
    reply_msg = str(group_msg_event.raw_message)  # 获取row_message
    reply_msg_id = re.findall(r"id=(.+?)]", reply_msg)
    replay_user_id = re.findall(
        r"qq=(.+?)]", reply_msg
    )  # 根据row_message中是否包含 reply id= 判断是否回复特定消息

    if (
        reply_msg_id and replay_user_id[0] == "320785209"
    ):  # 根据row_message中是否包含 at qq= 判断是否回复特定消息
        save_to_sqlite(
            "./msg/" + "answer.db", reply_msg_id[0], sender_id, group_msg
        )  
    else:
        save_to_sqlite(
            "./msg/" + "savemsg.db", "null", sender_id, group_msg
        )  

    # if group_msg == "/问题":  # 根据消息内容，判断回复什么
    #     await reply.finish("question1, question2, question3")  # 发送消息，并结束该事件
    # elif group_msg == "/help":
    #     await reply.finish('Please send "问题" to me')
    # else:
    #     await reply.finish()


def save_to_sqlite(file_name, question_id, qq_number, user_content):  # 消息保存到sqlite数据库
    tab_name = "ans_" + str(datetime.date.today().__format__("%Y%m%d"))
    create_tab = (
        "CREATE TABLE IF NOT EXISTS '%s'(QUES_ID int, QQ_NUM int, USER_CON text)"
        % (tab_name)
    )
    add_data = "INSERT INTO '%s'(QUES_ID, QQ_NUM, USER_CON) VALUES (%s ,%d, '%s')" % (
        tab_name,
        question_id,
        qq_number,
        user_content,
    )
    with sqlite3.connect(file_name) as db_con:
        db_con.execute(create_tab)
        db_con.execute(add_data)


def get_data_from_db(db_file_name, tab_name):
    get_data_sql = "SELECT QUES_ID, QQ_NUM, USER_CON FROM '%s'" % (tab_name)
    db_con = sqlite3.connect(db_file_name)
    db_cursor = db_con.cursor()
    db_cursor.execute(get_data_sql)
    data = db_cursor.fetchall()
    return data
