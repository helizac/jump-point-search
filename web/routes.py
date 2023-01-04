import json
import numpy as np

from flask import render_template, redirect, request
from jump_point_search import *
from web import app

grid = create_empty_grid(26, 14)

path = []

@app.route("/", methods = ["GET", "POST"])
def index():
    return render_template("home.html", grid=grid)

@app.route('/process_data', methods=['GET', 'POST'])
def process_data():
    global path

    grid = request.form.getlist('grid[]')
    grid = [grid[(i*len(grid))//14:((i+1)*len(grid))//14] for i in range(14)]
    grid = [[int(i) for i in j] for j in grid]
    path = jump_point_search(grid, 3, 3, 22, 10)
    path = get_full_path(path)

    return path

@app.route('/update_data', methods=['GET','POST'])
def update_data():

    key = request.args.get('reset')

    global grid
    return grid