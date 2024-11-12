from flask import jsonify, request
from models.TaskModel import Task
from config import db

def create_task():
    data = request.get_json()
    
    if not data or not all(k in data for k in ('description', 'employee_id')):
        return jsonify({'message': 'Description and employee_id are required fields'}), 400
    
    task = Task(
        description=data['description'],
        employee_id=data['employee_id']
    )
    
    db.session.add(task)
    db.session.commit()
    
    return jsonify({
        'id': task.id,
        'description': task.description,
        'employee_id': task.employee_id
    }), 201

def get_all_tasks():
    tasks = Task.query.all()
    
    if not tasks:
        return jsonify({'message': 'No tasks found'}), 404
    
    task_list = [{
        'id': task.id,
        'description': task.description,
        'employee_id': task.employee_id
    } for task in tasks]
    
    return jsonify(task_list), 200

def get_task(id):
    task = Task.query.get(id)
    
    if task:
        return jsonify({
            'id': task.id,
            'description': task.description,
            'employee_id': task.employee_id
        }), 200
    
    return jsonify({'message': f'Task with ID {id} not found'}), 404

def update_task(id):
    task = Task.query.get(id)
    
    if task:
        data = request.get_json()
        
        task.description = data.get('description', task.description)
        task.employee_id = data.get('employee_id', task.employee_id)
        
        db.session.commit()
        
        return jsonify({
            'id': task.id,
            'description': task.description,
            'employee_id': task.employee_id
        }), 200
    
    return jsonify({'message': f'Task with ID {id} not found'}), 404

def delete_task(id):
    task = Task.query.get(id)
    
    if task:
        db.session.delete(task)
        db.session.commit()
        return jsonify({'message': f'Task with ID {id} deleted successfully'}), 200
    
    return jsonify({'message': f'Task with ID {id} not found'}), 404
