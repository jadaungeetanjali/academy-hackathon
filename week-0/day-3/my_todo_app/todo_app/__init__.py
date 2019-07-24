import os

from flask import Flask
from flask import request

from flask import render_template

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    def get_todos_by_name(name):
        if name == 'geetanjali':
           return ['running', 'listen music']
        elif name == 'shivang':
           return ['wake up', 'coffee']
        elif name == 'dark':
           return ['counter strike']
        else:
           return []

    # http://127.0.0.1:5000/todos?name=geetanjali
    @app.route('/todos')
    def todos():
        name = request.args.get('name')
        print('----------')
        print(name)
        print('----------')

        person_todo_list = get_todos_by_name(name)
        #return todo_view(person_todo_list)
        return render_template('todo_view.html', todos=person_todo_list)

    return app

