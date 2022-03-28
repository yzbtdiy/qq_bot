import sqlite3, datetime


que_tab = "que_" + str(datetime.date.today().__format__("%Y%m%d"))
ans_tab = "ans_" + str(datetime.date.today().__format__("%Y%m%d"))


def save_que(file_name, question_id, question_txt):
    create_tab = (
        "CREATE TABLE IF NOT EXISTS '%s'(ID INTEGER PRIMARY KEY AUTOINCREMENT, QUES_ID text, QUES_TXT text, ADOPT_ANS text DEFAULT 'None')"
        % (que_tab)
    )
    add_data = "INSERT INTO '%s'(ID, QUES_ID, QUES_TXT) VALUES (NULL, '%s', '%s')" % (
        que_tab,
        question_id,
        question_txt,
    )
    with sqlite3.connect(file_name) as db_con:
        db_con.execute(create_tab)
        db_con.execute(add_data)


def save_ans(file_name, answer_id, qq_number, answer_txt, question_id):
    create_tab = (
        "CREATE TABLE IF NOT EXISTS '%s'(ID INTEGER PRIMARY KEY AUTOINCREMENT, ANS_ID text, QQ_NUM int, ANS_TXT text, QUES_ID text, IS_ADOPT text DEFAULT 'None')"
        % (ans_tab)
    )
    add_data = (
        "INSERT INTO '%s'(ANS_ID, QQ_NUM, ANS_TXT, QUES_ID) VALUES ('%s' ,%d, '%s', '%s')"
        % (ans_tab, answer_id, qq_number, answer_txt, question_id)
    )
    with sqlite3.connect(file_name) as db_con:
        db_con.execute(create_tab)
        db_con.execute(add_data)


def get_que(db_file):
    get_data_sql = "SELECT QUES_ID, QUES_TXT, ADOPT_ANS FROM '%s' ORDER BY ID DESC" % (
        que_tab
    )
    db_con = sqlite3.connect(db_file)
    db_cursor = db_con.cursor()
    db_cursor.execute(get_data_sql)
    data = db_cursor.fetchall()
    db_cursor.close()
    db_con.close()
    return data


# def get_rec_que(db_file):
#     get_data_sql = "SELECT QUES_TXT FROM '%s' ORDER BY ID DESC LIMIT 0,5" % (que_tab)
#     db_con = sqlite3.connect(db_file)
#     db_cursor = db_con.cursor()
#     db_cursor.execute(get_data_sql)
#     data = db_cursor.fetchall()
#     db_cursor.close()
#     db_con.close()
#     return data


def get_ans(db_file, quest_id):
    get_data_sql = (
        "SELECT ANS_ID, QQ_NUM, ANS_TXT, QUES_ID, IS_ADOPT FROM '%s' WHERE QUES_ID = '%s'"
        % (
            ans_tab,
            quest_id,
        )
    )
    db_con = sqlite3.connect(db_file)
    db_cursor = db_con.cursor()
    db_cursor.execute(get_data_sql)
    data = db_cursor.fetchall()
    db_cursor.close()
    db_con.close()
    return data


def update_que(db_file, quest_id, answer_id):
    update_sql = "UPDATE '%s' SET ADOPT_ANS = '%s' WHERE QUES_ID = '%s'" % (
        que_tab,
        answer_id,
        quest_id,
    )
    with sqlite3.connect(db_file) as db_con:
        db_cursor = db_con.cursor()
        db_cursor.execute(update_sql)


def update_ans(db_file, is_adopt, answer_id):
    reset_sql = "UPDATE '%s' SET IS_ADOPT = '未采用' WHERE IS_ADOPT = '采用'" % (ans_tab)
    update_sql = "UPDATE '%s' SET IS_ADOPT = '%s' WHERE ANS_ID = '%s'" % (
        ans_tab,
        is_adopt,
        answer_id,
    )
    with sqlite3.connect(db_file) as db_con:
        db_cursor = db_con.cursor()
        db_cursor.execute(reset_sql)
        db_cursor.execute(update_sql)
