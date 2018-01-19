# app/backend.py
from flask import Blueprint
from flask_restful import Api


api_bp = Blueprint('backend', __name__)
api = Api(api_bp)


from app.tasks import TaskListAPI, TaskAPI


# Register the endpoint to the api
api.add_resource(TaskListAPI, '/get-tasks')
api.add_resource(TaskAPI, '/get-task/<int:id>')

