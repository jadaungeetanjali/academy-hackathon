import os

from flask import Flask
from flask import request

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    def todo_view(todos):
        the_view = 'List of my todos:' + '<br/>'
        for todo in todos:
            the_view += (todo) + '<br/>'

        the_view += '---List Ends Here---' + '<br/>'
        return the_view

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
        return todo_view(person_todo_list)

    @app.route('/geetanjali')
    def geetanjali():
        my_todos = ['running', 'listen music']
        return todo_view(my_todos)
	
    # a simple page that list my todos
    @app.route('/shivang')
    def shivang():
        my_todos = ['wake up', 'coffee']
        return todo_view(my_todos)

    return app

