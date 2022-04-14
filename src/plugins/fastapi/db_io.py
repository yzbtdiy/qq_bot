import sqlite3, datetime


# db_name = "./msg/" + str(datetime.date.today().__format__("%Y%m%d")) + ".db"

db_name = "./msg/20220331.db"


def db_init():
    add_que_tab = "CREATE TABLE IF NOT EXISTS questions (ID INTEGER PRIMARY KEY AUTOINCREMENT, QUE_ID TEXT, QUE_TXT TEXT, ADOPT_ANS TEXT DEFAULT 'None', G_ID INTEGER DEFAULT 'None')"
    add_ans_tab = "CREATE TABLE IF NOT EXISTS answers (ID INTEGER PRIMARY KEY AUTOINCREMENT, ANS_ID TEXT, QQ_NUM int, ANS_TXT TEXT, QUE_ID TEXT, IS_ADOPT TEXT DEFAULT 'None')"
    with sqlite3.connect(db_name) as db_con:
        db_con.execute(add_que_tab)
        db_con.execute(add_ans_tab)


def save_que(que_id, que_txt, g_id=None):
    add_sql = (
        "INSERT INTO questions (ID, QUE_ID, QUE_TXT) VALUES (NULL, '%s', '%s')"
        % (
            que_id,
            que_txt,
        )
    )
    with sqlite3.connect(db_name) as db_con:
        db_con.execute(add_sql)
        db_cursor = db_con.cursor()
        if g_id:
            update_sql = "UPDATE questions SET G_ID = %d WHERE QUE_ID = '%s'" % (
                g_id,
                que_id,
            )
        else:
            get_index = "SELECT ID FROM questions WHERE QUE_ID = '%s'" % que_id
            db_cursor.execute(get_index)
            index = db_cursor.fetchall()[0][0]
            update_sql = "UPDATE questions SET G_ID = %d WHERE QUE_ID = '%s'" % (
                index,
                que_id,
            )
        db_con.execute(update_sql)


def get_gid(ans_id):
    get_sql = (
        "SELECT q.G_ID, q.QUE_ID FROM questions AS q INNER JOIN answers AS a WHERE a.ANS_ID = '%s' AND q.QUE_ID = a.QUE_ID"
        % ans_id
    )
    with sqlite3.connect(db_name) as db_con:
        db_cursor = db_con.cursor()
        db_cursor.execute(get_sql)
        g_id = db_cursor.fetchall()[0][0]
    return g_id


def save_ans(ans_id, qq_num, ans_txt, que_id):
    add_sql = (
        "INSERT INTO answers (ANS_ID, QQ_NUM, ANS_TXT, QUE_ID) VALUES ('%s' ,%d, '%s', '%s')"
        % (ans_id, qq_num, ans_txt, que_id)
    )
    with sqlite3.connect(db_name) as db_con:
        db_con.execute(add_sql)


def get_que():
    get_sql = (
        "SELECT QUE_ID, QUE_TXT, ADOPT_ANS, G_ID FROM questions ORDER BY G_ID DESC"
    )
    with sqlite3.connect(db_name) as db_con:
        db_cursor = db_con.cursor()
        db_cursor.execute(get_sql)
        data = db_cursor.fetchall()
    return data


def get_ans(que_id):
    get_sql = (
        "SELECT ANS_ID, QQ_NUM, ANS_TXT, QUE_ID, IS_ADOPT FROM answers WHERE QUE_ID = '%s'"
        % (que_id,)
    )
    with sqlite3.connect(db_name) as db_con:
        db_cursor = db_con.cursor()
        db_cursor.execute(get_sql)
        data = db_cursor.fetchall()
    return data


def update_que(que_id, ans_id):
    update_sql = "UPDATE questions SET ADOPT_ANS = '%s' WHERE QUE_ID = '%s'" % (
        ans_id,
        que_id,
    )
    with sqlite3.connect(db_name) as db_con:
        db_cursor = db_con.cursor()
        db_cursor.execute(update_sql)


def update_ans(is_adopt, ans_id):
    reset_sql = "UPDATE answers SET IS_ADOPT = 'None' WHERE IS_ADOPT = '采用'"
    update_sql = "UPDATE answers SET IS_ADOPT = '%s' WHERE ANS_ID = '%s'" % (
        is_adopt,
        ans_id,
    )
    with sqlite3.connect(db_name) as db_con:
        db_cursor = db_con.cursor()
        db_cursor.execute(reset_sql)
        db_cursor.execute(update_sql)


def get_num(count_item):
    if count_item == "que_num":
        count_sql = "SELECT COUNT(*) FROM questions"
    elif count_item == "ans_num":
        count_sql = "SELECT COUNT(*) FROM answers"
    elif count_item == "solve_que":
        count_sql = "SELECT COUNT(*) FROM questions WHERE NOT ADOPT_ANS='None'"
    with sqlite3.connect(db_name) as db_con:
        db_cursor = db_con.cursor()
        db_cursor.execute(count_sql)
        data = db_cursor.fetchall()
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
