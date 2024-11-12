from flask import jsonify, request
from models.TaskModel import Task
from config import db

# Function to create a new task
def create_task():
    # Get the data from the request body (JSON format)
    data = request.get_json()
    
    # Validate the data
    if not data or not all(k in data for k in ('description', 'employee_id')):
        return jsonify({'message': 'Description and employee_id are required fields'}), 400
    
    # Create a new Task object using the provided data
    task = Task(
        description=data['description'],
        employee_id=data['employee_id']
    )
    
    # Add the new task to the session and commit it to the database
    db.session.add(task)
    db.session.commit()
    
    # Return the created task object as JSON
    return jsonify({
        'id': task.id,
        'description': task.description,
        'employee_id': task.employee_id
    }), 201

# Function to get all tasks
def get_all_tasks():
    # Retrieve all tasks from the database
    tasks = Task.query.all()
    
    # If no tasks found, return a message
    if not tasks:
        return jsonify({'message': 'No tasks found'}), 404
    
    # Convert each task to a dictionary and return as JSON
    task_list = [{
        'id': task.id,
        'description': task.description,
        'employee_id': task.employee_id
    } for task in tasks]
    
    return jsonify(task_list), 200

# Function to get a specific task by ID
def get_task(id):
    # Retrieve a specific task based on the provided ID
    task = Task.query.get(id)
    
    if task:
        return jsonify({
            'id': task.id,
            'description': task.description,
            'employee_id': task.employee_id
        }), 200
    
    return jsonify({'message': f'Task with ID {id} not found'}), 404

# Function to update an existing task by ID
def update_task(id):
    # Retrieve the task object to update
    task = Task.query.get(id)
    
    if task:
        # Get the data from the request body
        data = request.get_json()
        
        # Update the fields with the data provided
        task.description = data.get('description', task.description)
        task.employee_id = data.get('employee_id', task.employee_id)
        
        # Commit the changes to the database
        db.session.commit()
        
        return jsonify({
            'id': task.id,
            'description': task.description,
            'employee_id': task.employee_id
        }), 200
    
    return jsonify({'message': f'Task with ID {id} not found'}), 404

# Function to delete a task by ID
def delete_task(id):
    # Retrieve the task to delete
    task = Task.query.get(id)
    
    if task:
        # Delete the task from the session and commit the change
        db.session.delete(task)
        db.session.commit()
        return jsonify({'message': f'Task with ID {id} deleted successfully'}), 200
    
    return jsonify({'message': f'Task with ID {id} not found'}), 404
