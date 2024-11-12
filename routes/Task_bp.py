from flask import Blueprint
from controllers.TaskController import create_task, get_all_tasks, get_task, update_task, delete_task

task_bp = Blueprint('task_bp', __name__)

# Route for getting all tasks
task_bp.route('/api/tasks', methods=['GET'])(get_all_tasks)

# Route for getting a specific task by ID
task_bp.route('/api/task/<int:id>', methods=['GET'])(get_task)

# Route for creating a new task
task_bp.route('/api/task', methods=['POST'])(create_task)

# Route for updating an existing task by ID
task_bp.route('/api/task/<int:id>', methods=['PUT'])(update_task)

# Route for deleting a task by ID
task_bp.route('/api/task/<int:id>', methods=['DELETE'])(delete_task)
