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

    @app.route('/todos')
    def todos():
        name = request.args.get('name')
        print(name)
        return todo_view([])
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

