from msilib.schema import InstallUISequence
import re
from typing import Union

# from nonebot.adapters.onebot.v11 import Bot, Event, PrivateMessageEvent, GroupMessageEvent
from nonebot.adapters.onebot.v11 import GroupMessageEvent
from nonebot.plugin import on_message


def save_to_file(file_name, contents):
    stf = open(file_name, 'a+')
    stf.write(contents + '\n')
    stf.close()
  
# def msg_classify(user_msg):
#     write_to_file = "savemsg"
#     if re.search(r"1.$", user_msg):
#         write_to_file = "1.txt"
#     if re.search(r"2.$", user_msg):
#         write_to_file = "2.txt"
#     if re.search(r"3.$", user_msg):
#         write_to_file = "3.txt"
#     return write_to_file

reply = on_message(priority=100)                #注册事件响应器，优先度很低
@reply.handle()                                 #调用装饰器

# async def reply_handle(bot: Bot, event: Event): #创建事件处理函数
    
#     user_msg = str(event.get_message()).strip() #获取消息内容

#     file_name = msg_classify(user_msg)
    
#     save_to_file(file_name, user_msg)

# async def rec_group_msg(group_msg_event: GroupMessageEvent):
#     group_msg = group_msg_event.get_plaintext()
#     if isinstance(group_msg_event.raw_message, dict):
#         reply_msg = group_msg_event.raw_message[0]
#         reply_msg_id = re.findall(r'id=(.+?)]', reply_msg)
#         save_to_file('./msg/' + str(reply_msg_id), group_msg)
#     else:
#         save_to_file('./msg/' + 'savemsg', group_msg)

        
async def rec_group_msg(group_msg_event: GroupMessageEvent):
    group_msg = group_msg_event.get_plaintext()
    reply_msg = str(group_msg_event.raw_message)
    reply_msg_id = re.findall(r'id=(.+?)]', reply_msg)
    if reply_msg_id:        
        save_to_file('./msg/' + str(reply_msg_id[0]) + '.txt', group_msg)
    else:
        save_to_file('./msg/' + 'savemsg', group_msg)


    # reply_msg_id = group_msg_event.raw_message[0]
    # group_msg = str(group_msg_event.get_message()).strip()
    # file_name = msg_classify(group_msg)
    # file_name = str(group_msg_id) + '.txt'
    # save_to_file('./msg/' + file_name, group_msg_id)
    # save_to_file('./msg/' + str(reply_msg_id), group_msg)



    # save_to_file('msgsave', user_msg)           #保存获取的消息到文件
    
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


# from typing import Union
# from nonebot import get_driver
# from nonebot.adapters import Bot, Event
# from nonebot.adapters.onebot.v11 import Bot as OneBot
# from nonebot.adapters.onebot.v11 import PrivateMessageEvent, GroupMessageEvent
# from .config import Config

# global_config = get_driver().config
# config = Config.parse_obj(global_config)

# async def recMsg(foo: Union[PrivateMessageEvent, GroupMessageEvent]): ...

# print(recMsg)
# Export something for other plugin
# export = nonebot.export()
# export.foo = "bar"

# @export.xxx
# def some_function():
#     pass

