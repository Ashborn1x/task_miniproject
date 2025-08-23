# routes/tasks.py
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from extensions import db
from models import Task

tasks_bp = Blueprint("tasks", __name__)

# ✅ Get all tasks for current user
@tasks_bp.route("/tasks", methods=["GET"])
@jwt_required()
def get_tasks():
    user_id = get_jwt_identity()
    tasks = Task.query.filter_by(user_id=user_id).all()
    return jsonify([{"id": t.id, "title": t.title, "completed": t.done} for t in tasks])

# ✅ Create a new task
@tasks_bp.route("/tasks", methods=["POST"])
@jwt_required()
def create_task():
    user_id = get_jwt_identity()
    data = request.get_json()
    new_task = Task(title=data["title"], done=False, user_id=user_id)
    db.session.add(new_task)
    db.session.commit()
    return jsonify({
        "id": new_task.id,
        "title": new_task.title,
        "completed": new_task.done
    }), 201

# ✅ Update a task
@tasks_bp.route("/tasks/<int:task_id>", methods=["PUT"])
@jwt_required()
def update_task(task_id):
    user_id = get_jwt_identity()
    task = Task.query.filter_by(id=task_id, user_id=user_id).first()
    if not task:
        return jsonify({"msg": "Task not found"}), 404
    data = request.get_json()
    task.title = data.get("title", task.title)
    task.done = data.get("completed", task.done)   # 👈 accept completed
    db.session.commit()
    return jsonify({
        "id": task.id,
        "title": task.title,
        "completed": task.done
    })

# ✅ Delete a task
@tasks_bp.route("/tasks/<int:task_id>", methods=["DELETE"])
@jwt_required()
def delete_task(task_id):
    user_id = get_jwt_identity()
    task = Task.query.filter_by(id=task_id, user_id=user_id).first()
    if not task:
        return jsonify({"msg": "Task not found"}), 404
    db.session.delete(task)
    db.session.commit()
    return jsonify({"msg": "Task deleted"})
