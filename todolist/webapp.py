from flask import redirect, url_for, render_template, request
from model import app, Task
import model

@app.route("/")
def home():
    return_str = ""
    tasks = Task.query.all()
    return render_template("list_tasks.html", tasks=tasks)


@app.route("/add", methods=["GET"])
def make_task():
	return render_template("make_tasks.html")

@app.route("/add", methods=["POST"])
def save_task():
	new_task = Task(request.form['title'])
	model.add(new_task)
	model.save_all()
	return "Saved this task"


@app.route("/edit/<int:task_id>")
def edit_task(task_id):
	task = Task.query.get(task_id)
	return "You entered %d in your url, %s"%(task_id, task)

# @app.route("/completed", methods=["POST"])
# def completed_task():
# 	completed_task = Task.complete(request.for)

# 	return "Marked this task completed."



