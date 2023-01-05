# Jump Point Search Implementation

This repository is a Python implementation of Jump Point Search Algorithm on Flask website.

<sub>Note: For this repository, Jump Point Search Algorithm is implemented in a corner pass-through version. And taken advancing each unit costs 1, advancing diagonals costs 2^(1/2).</sub>

<br>

<div align="center">
    <img src="https://user-images.githubusercontent.com/54884571/210841925-b975b88a-8177-4aa4-b7e1-6457aeb13480.gif" height="56"/>
    <img src="https://user-images.githubusercontent.com/54884571/210841922-639ff133-9123-4eef-a38c-3cc7f6f844f5.gif" height="40"/>
</div>

## Contents

<div>
    <ul>
        <li><a href="#introduction">Introduction</a></li>
        <li><a href="#project-architecture">Project Architecture</a></li>
        <li><a href="jps">Detailed Jump Point Search Algoritm</a></li>
        <li><a href="#results">Results</a></li>
        <li><a href="#conclusion">Conclusion</a></li>
        <li><a href="#references">References</a></li>
    </ul>
</div>

<h2 id="introduction">Introduction</h2>

Jump Point Search Algorithm is very efficient especially in dungeon games or the areas with many obstacles. That's why I used an dungeon theme in the website. For the sake of the mushroom characters who have been crushed for years, a powerful mushroom is chasing Mario on the website. With the JPS algorithm, Mario can escape from the mushroom.

#### What's Jump Point Search Algorithm?

Jump point search (JPS) is a pathfinding algorithm for graphs that is an optimization of the A* search algorithm. It is designed to efficiently find a shortest path between two points in a graph that has many more possible paths than just the straight line distance between the two points. The algorithm works by "jumping" over nodes in the graph that are unlikely to be on the optimal path, using pre-computed "jump points" to quickly move closer to the goal. This can greatly reduce the number of nodes that need to be evaluated, making the search much faster than a standard A* search. JPS is particularly well-suited for use in grid-based graphs, such as those used in many video games and robotics applications.

<h2 id="project-architecture">Project Architecture</h2>

```
- .github
    - workflow
        + static.yml # To display static page in Github
- web
    - static
        - css
            + style.css # contains some style file for home.html ( also has animations inside )
        - js 
            + grid.js # creates grids and handle grid events. Also handles animations.
            + lottie.js # a simple lottie integration file for easy use. 
        - lottie
            + animation1.gif
            + fireworks.json
            + mario.gif
            + mushroom.gif
            + paper.json
            + tile.png
    - templates
        + home.html # main page ( also sends data to back-end and takes the grid answer after jump-point-search ) 
    + __init__.py # handles Flask and config properties
    + routes.py # basic Flask routing page that contact with front-end to find the path.
+ .gitattributes
+ .gitignore
+ LICENSE
+ jump_point_search.py # Jump Point Search implementation file
+ main.py # main file to run all the codes above
+ readme.md
```

For this project there are just two libraries that need to be installed in the terminal. Use pip3 or pip for install packages.

To simply install libraries type after open the cmd in jump-point-search file ->
```
pip install -r requirements.txt
```

and that will install immediatly ->
```
Flask==2.2.2
numpy==1.23.5
```

After that type ->
```
python main.py
```

And voilà. A link will open in your browser. ( If not, ctrl+click on the url. )

<h2 id="jps">Detailed Jump Point Search Algoritm</h2>

The algorithm starts at the starting node and adds it to the open list. The open list is a list of nodes that are being considered for expansion. It repeats the following steps until the open list is empty.

1) The algorithm gets the node with the lowest cost (F value) from the open list. The F value is an estimate of the cost to reach the goal from a given node, using the Manhattan distance heuristic.
2) If the node is the goal, the algorithm returns the path from the starting node to the goal.
3) If the node is not the goal, the algorithm expands it by generating its successors. A successor is a node that can be reached from the current node in one step.
4) For each successor, the algorithm does the following:

    a) If the successor is the goal, the algorithm returns the path from the starting node to the goal.
    
    b) If the successor is not in the open list or closed list, the algorithm adds it to the open list and sets its parent to the current node. The closed list is a list of nodes that have already been expanded.
    
    c) If the successor is in the open list, the algorithm checks if the current path to the successor is better than the previous path. If it is, the algorithm updates the successor's parent to the current node.
    
5) The algorithm adds the current node to the closed list.

#### Example

Let's assume that we have an green start point and we want to reach to the red point.

At this point algorithm starts to search and we obtain: from green point, we search 8 direction ( top, bottom, left, right, top left, top right, bottom left, bottom right ) and for each direction, if the direction is diagonal, it scans vertical and horizontal space in its direction like below.

Then the shortest path is returned.

<div align="center"><img src="https://user-images.githubusercontent.com/54884571/210862898-bee6061a-aac5-43ba-b1ea-2a0894630f02.png" width ="50%"></div>

For an another example with an obstacle,

in the first iteration algorithm couldn't find the red point, so it jumps to the corner which is the closest corner to reach point and continue to search again. Remember that in this implementation, advancing each unit costs 1, advancing diagonals costs 2^(1/2).


<div align="center"><img src="https://user-images.githubusercontent.com/54884571/210863842-a0d3c691-33b0-47dd-9cbf-7d41b45f537a.png" width ="50%"></div>

<h2 id="results">Results</h2>

When we run the whole program and click to "Find Route" we can obtain the results of the Jump Point Search Algorithm.

|     |     |     |     |     |     |     |     |     |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|||||<video src="https://user-images.githubusercontent.com/54884571/210867028-430cd3c7-02f1-441a-b499-58de2fcd4b7f.mp4" frameborder="0" allowfullscreen="true"></video>|||||

<h2 id="conclusion">Conclusion</h2>

Jump point search is often used in video games and robotics applications where there is a need to find a shortest path through a grid-based environment. In these cases, JPS can be used to quickly and efficiently find a path through the grid while avoiding obstacles.

JPS is also used in other applications where there is a need to find a shortest path through a graph with many possible paths, such as in transportation and logistics planning. In these cases, the algorithm can be used to find the most efficient route for a delivery truck or other vehicle to take, taking into account factors such as traffic conditions and road network structure.

Overall, JPS is a useful algorithm for finding a shortest path through a graph when the graph is large or when there are many possible paths that need to be considered. Its efficiency makes it well-suited for use in a variety of applications where pathfinding is important.

<h2 id="references">References</h2>

Special thanks to Daniel Harabor and Alban Grastien whom introduces the JPS algorithm formally and serves as an excellent reference when implementing the algorithm for yourself.

Also thanks to Nathan Witmer who implemented this algorithm on a very explanatory and inspiring site.

Finally thanks to my best friend for design ideas <div align="center"><img src="https://user-images.githubusercontent.com/54884571/210874888-ae0d86c5-f990-4f87-9556-2429ad1a8f64.png" height="20"></div>


[1] https://users.cecs.anu.edu.au/~dharabor/data/papers/harabor-grastien-icaps14.pdf

[2] https://zerowidth.com/2013/a-visual-explanation-of-jump-point-search.html
