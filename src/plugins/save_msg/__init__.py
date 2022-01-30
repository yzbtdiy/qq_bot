from nonebot.adapters.onebot.v11 import GroupMessageEvent
from nonebot.plugin import on_message
import re, sqlite3

# from nonebot.adapters.onebot.v11 import Bot, Event, PrivateMessageEvent, GroupMessageEvent

# def save_to_file(file_name, contents):  # 文件保存到本地
#     stf = open(file_name, "a+")  # 追加文件内容
#     stf.write(contents + "\n")
#     stf.close()


# def save_to_file(file_name, qq_number, user_content):  # 文件保存到本地
#     with open(file_name, "a+", encoding="utf-8") as f:  # 追加文件内容
#         if f.read() == "":
#             data = {}
#         else:
#             data = json.load(f)
#         data["qq"] = qq_number
#         data["content"] = user_content
#         # f.write(data + "\n")
#         json.dump(data, f, indent=6)
#         f.close()


# async def send_group_info(bot: Bot):
#     send_result = bot.send_group_msg(group_id = 755048599, message="send_msg")


# async def send_group_info(bot: Bot, event: Event):
#     await reply.send("hello, world")
# res = bot.send_group_msg(group_id = 755048599, message="send_msg")
# save_to_file('./msg/' +'sendres.txt',res)


# matcher = on_command("hello")
# @matcher.handle()
# async def handle_hello(bot: Bot, event: Event):
#     # 发送信息
#     await matcher.send("question1")
#     # 或者通过 bot
#     await bot.send(event, "question2")


def save_to_sqlite(file_name, qq_number, user_content):  # 消息保存到sqlite数据库
    with sqlite3.connect(file_name) as db_con:
        db_con.execute(
            """
            CREATE TABLE IF NOT EXISTS msg_save(
	        QQ_NUM int,
	        USER_CON text
            )
            """
        )
        sql = "INSERT INTO msg_save(QQ_NUM, USER_CON) VALUES (%d, '%s')" % (
            qq_number,
            user_content,
        )
        db_con.execute(sql)

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
            "./msg/" + str(reply_msg_id[0]) + ".db", sender_id, group_msg
        )  # 回复类消息内容保存到 id.txt 文件中
    else:
        save_to_sqlite(
            "./msg/" + "savemsg.db", sender_id, group_msg
        )  # 非回复类消息内容保存到 savemsg.txt 文件中

    if group_msg == "/问题":  # 根据消息内容，判断回复什么
        await reply.finish("question1, question2, question3")  # 发送消息，并结束该事件
    elif group_msg == "/help":
        await reply.finish('Please send "问题" to me')
    else:
        await reply.finish()


# def msg_classify(user_msg):
#     write_to_file = "savemsg"
#     if re.search(r"1.$", user_msg):
#         write_to_file = "1.txt"
#     if re.search(r"2.$", user_msg):
#         write_to_file = "2.txt"
#     if re.search(r"3.$", user_msg):
#         write_to_file = "3.txt"
#     return write_to_file

# async def reply_handle(bot: Bot, event: Event): #创建事件处理函数
#     user_msg = str(event.get_message()).strip() #获取消息内容
#     file_name = msg_classify(user_msg)
#     save_to_file(file_name, user_msg)

# if re.search(r"1.$", user_msg):
#     await save_to_file('msgsave1', user_msg)
# if re.search(r"2.$", user_msg):
#     await save_to_file('msgsave2', user_msg)
# if re.search(r"3.$", user_msg):
#     await save_to_file('msgsave3', user_msg)

# if user_msg == '123':                       #根据消息内容，判断回复什么
#     await reply.finish('456')               #发送消息，并结束该事件
# elif user_msg == 'hello':
#     await reply.finish('world')
# else:
#     await reply.finish()

# async def rec_group_msg(group_msg_event: GroupMessageEvent):
#     group_msg = group_msg_event.get_plaintext()
#     if isinstance(group_msg_event.raw_message, dict):
#         reply_msg = group_msg_event.raw_message[0]
#         reply_msg_id = re.findall(r'id=(.+?)]', reply_msg)
#         save_to_file('./msg/' + str(reply_msg_id), group_msg)
#     else:
#         save_to_file('./msg/' + 'savemsg', group_msg)


############# Default Content ################
# from nonebot import get_driver

# from .config import Config

# global_config = get_driver().config
# config = Config.parse_obj(global_config)

# Export something for other plugin
# export = nonebot.export()
# export.foo = "bar"

# @export.xxx
# def some_function():
#     pass
