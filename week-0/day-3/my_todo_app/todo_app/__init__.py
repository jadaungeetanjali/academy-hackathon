import os

from flask import Flask
from flask import request

from flask import render_template

todo_store = {}
todo_store['geetanjali'] = ['sleep', 'sleep', 'sleep']
todo_store['shivang'] = ['wake up', 'coffee']
todo_store['nitin'] = ['running', 'listen music']
todo_store['dark'] = ['counter strike']

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    def select_todos(name):
        global todo_store
        return todo_store[name]

    def insert_todos(name, todo):
        global todo_store
        print(todo)
        current_todos = todo_store[name]
        current_todos.append(todo)
        todo_store[name] = current_todos
        return

    def add_todo_by_name(name, todo):
        #call DB function
        insert_todos(name, todo)
        return 

    def get_todos_by_name(name):
        return select_todos(name)

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

    @app.route('/add_todos')
    def add_todos():
        name = request.args.get('name')
        todo = request.args.get('todo')
        add_todo_by_name(name, todo)
        return 'Added Successfully'

    return app

