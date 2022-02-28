# from flask import Flask, request, render_template, redirect, session, url_for, g
# from dataclasses import dataclass
# import sqlite3, datetime

# from nonebot.plugin import export
# import subprocess
# from multiprocessing import Process, freeze_support


# app = Flask(__name__, static_url_path="/")
# app.config["SECRET_KEY"] = "T7tj6whdT4eKmIZ3"


# def save_to_sqlite(file_name, question):  # 保存问题到数据库
#     tab_name = "ans" + str(datetime.date.today().__format__("%Y%m%d"))
#     create_tab = (
#         "CREATE TABLE IF NOT EXISTS '%s'(ID INTEGER PRIMARY KEY AUTOINCREMENT, QUES_TXT text)"
#         % (tab_name)
#     )
#     add_data = "INSERT INTO '%s'(ID, QUES_txt) VALUES (NULL, '%s')" % (
#         tab_name,
#         question,
#     )
#     with sqlite3.connect(file_name) as db_con:
#         db_con.execute(create_tab)
#         db_con.execute(add_data)


# def get_data_from_db(db_file_name, tab_name):  # 从数据库中获取答案
#     get_data_sql = "SELECT QUES_ID, QQ_NUM, USER_CON FROM '%s'" % (tab_name)
#     db_con = sqlite3.connect(db_file_name)
#     db_cursor = db_con.cursor()
#     db_cursor.execute(get_data_sql)
#     data = db_cursor.fetchall()
#     return data


# @dataclass
# class User:
#     id: int
#     username: str
#     password: str


# users = [User(1, "admin", "admin"), User(2, "test", "test")]


# @app.before_request
# def before_request():
#     g.user = None
#     if "user_id" in session:
#         user = [u for u in users if u.id == int(session["user_id"])][0]
#         g.user = user


# @app.route("/login", methods=["GET", "POST"])
# def login():
#     if request.method == "POST":
#         session.pop("user_id", None)
#         username = request.form.get("username", None)
#         password = request.form.get("password", None)
#         user = [u for u in users if u.username == username]
#         if len(user) > 0:
#             user = user[0]
#         if user and user.password == password:
#             session["user_id"] = user.id
#             return redirect(url_for("profile"))
#     return render_template("login.html")


# @app.route("/profile")
# def profile():
#     if not g.user:
#         return redirect(url_for("login"))
#     return render_template("profile.html")


# @app.route("/add_question", methods=["GET", "POST"])
# def add_question():
#     if request.method == "POST":
#         question = request.form.get("question", None)
#         save_to_sqlite("./api/qusetion.db", question)

#         # user = [u for u in users if u.username == username]
#         # if len(user) > 0:
#         #     user = user[0]
#         # if user and user.password == password:
#         #     session["user_id"] = user.id
#         #     return redirect(url_for("profile"))
#     return render_template("question.html")


# @app.route("/get_answer")
# def get_answer():
#     if request.method == "GET":
#         g.data = get_data_from_db("./msg/answer.db", "20220220")
#         return render_template("answer.html", data=g.data)


# def run_web():
#     app.run()


# # freeze_support()
# # Process(target=run_web, args=()).start()

# # # export.web=app

# # # uvicorn.run(app=app)
# # if __name__ == "__main__":
# #     freeze_support()
