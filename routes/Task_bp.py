from flask import Blueprint
from controllers.TaskController import create_task, get_all_tasks, get_task, update_task, delete_task

task_bp = Blueprint('task_bp', __name__)

task_bp.route('/api/tasks', methods=['GET'])(get_all_tasks)

task_bp.route('/api/task/<int:id>', methods=['GET'])(get_task)

task_bp.route('/api/task', methods=['POST'])(create_task)

task_bp.route('/api/task/<int:id>', methods=['PUT'])(update_task)

task_bp.route('/api/task/<int:id>', methods=['DELETE'])(delete_task)
