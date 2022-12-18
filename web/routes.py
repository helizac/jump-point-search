import json

from flask import render_template, redirect, session, request
from jump_point_search import *
from web import app


@app.route("/", methods = ["GET", "POST"])
def index():
    if "grid" in session:
        grid = session["grid"]
    else:
        grid = None

    if request.method == "GET":
        reset = request.args.get("reset")
        if reset:
            session.clear()
            return redirect("/")

    return render_template("home.html", grid=grid)

@app.route("/ProcessInfo/<string:grid>", methods=["GET", "POST"])
def process(grid):
    grid=json.loads(grid)

    x_field = grid
    for i in range(len(x_field)):
        x_field[i].insert(0, -10)
        x_field[i].append(-10)
    x_field.insert(0, [-10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10])
    x_field.append([-10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10])
    
    field = x_field
    field[1][1] = UNINITIALIZED  # guarantee that the end is reachable
    field[11][23] = UNINITIALIZED

    try:
        drawGrid(field)
    except ImportError as err:
        print("You don't have pygame. Cannot display large test. ", err)
        
    path = jump_point_search(field, 3, 3, 9, 21)
    path = get_full_path(path)

    for i in range(len(path)):
        x_field[path[i][0]][path[i][1]] = -5

    del x_field[len(x_field)-1]
    del x_field[0]

    for i in range(len(x_field)):
        del x_field[i][len(x_field[i])-1]
        del x_field[i][0]

    session["grid"] = x_field

    return redirect("/")