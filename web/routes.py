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
        x_field[i].insert(0, BLOCK)
        x_field[i].append(BLOCK)
    x_field.insert(0, [BLOCK for x in range(26)])
    x_field.append([BLOCK for x in range(26)])
    
    field = x_field

    try:
        showField(field)
    except Exception as e:
        print(e)
        
    path = jump_point_search(field, 3, 3, 22, 10)
    path = get_full_path(path)

    del path[0]
    del path[-1]
    for i in range(len(path)):
        x_field[path[i][0]][path[i][1]] = 3

    del x_field[-1]
    del x_field[0]

    for i in range(len(x_field)):
        del x_field[i][-1]
        del x_field[i][0]

    session["grid"] = x_field

    return redirect("/")