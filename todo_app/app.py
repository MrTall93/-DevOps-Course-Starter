from flask import Flask, render_template, request, redirect, url_for
from todo_app.data.session_items import get_items, add_item
from todo_app.flask_config import Config
from todo_app.data.trello_items import get_todo, add_todo, update_itemList

app = Flask(__name__)
app.config.from_object(Config())

@app.route("/", methods=["POST","GET"])
def index():
    if request.method == "POST":
        title = request.form['title']
        add_todo(title)
    todo_list = get_todo()

    return render_template('index.html', data=todo_list)

@app.route("/done/<task_id>",methods=['GET'])
def done(task_id):
    update_itemList(task_id,'To Do')
    return redirect(url_for("index"))

@app.route("/undone/<task_id>",methods=['GET'])
def undone(task_id):
    update_itemList(task_id,'Done')
    return redirect(url_for("index"))

