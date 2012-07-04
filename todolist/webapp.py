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
	return redirect(url_for("home"))


@app.route("/edit/<int:task_id>", methods = ["GET"])
def edit_task(task_id):
	edit_task = Task.query.get(task_id)
	return render_template("edit_tasks.html", task=edit_task)

@app.route("/finished_tasks", methods = ["GET"])
def finished_task():
	return render_template("edit_tasks.html")

@app.route("/finished_tasks/<int:task_id>", methods=["POST"])
def save_finished_task(task_id):
	task = Task.query.get(task_id)
	if request.form.get("done"):
		task.complete()
	# new_task = Task.complete(finished_task())
	# model.add(new_task)
	model.save_all()
	return redirect(url_for("home"))


# @app.route("/completed", methods=["POST"])
# def completed_task():
# 	completed_task = Task.complete(request.for)

# 	return "Marked this task completed."



