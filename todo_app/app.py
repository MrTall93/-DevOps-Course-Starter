from flask import Flask, render_template, request
from todo_app.data.session_items import get_items, add_item
from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/', methods=['POST','GET'])
def index():
    if request.method == "POST":
        title = request.form['title']
        add_item(title)

    return render_template('index.html', data=get_items())


