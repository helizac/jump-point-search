# Jump Point Search Implementation

This repository is a Python implementation of Jump Point Search Algorithm on Flask website. You can try out by running <b>main.py</b>

<div align="center">
    <img src="https://user-images.githubusercontent.com/54884571/210841925-b975b88a-8177-4aa4-b7e1-6457aeb13480.gif" height="56"/>
    <img src="https://user-images.githubusercontent.com/54884571/210841922-639ff133-9123-4eef-a38c-3cc7f6f844f5.gif" height="40"/>
</div>

## Contents

<div>
    <ul>
        <li><a href="#introduction">Introduction</a></li>
        <li><a href="#project-architecture">Project Architecture</a></li>
        <li><a href="#results">Results</a></li>
        <li><a href="#conclusion">Conclusion and Future Work</a></li>
    </ul>
</div>

<h2 id="introduction">Introduction</h3>

#### What's Jump Point Search Algorithm?

Jump point search (JPS) is a pathfinding algorithm for graphs that is an optimization of the A* search algorithm. It is designed to efficiently find a shortest path between two points in a graph that has many more possible paths than just the straight line distance between the two points. The algorithm works by "jumping" over nodes in the graph that are unlikely to be on the optimal path, using pre-computed "jump points" to quickly move closer to the goal. This can greatly reduce the number of nodes that need to be evaluated, making the search much faster than a standard A* search. JPS is particularly well-suited for use in grid-based graphs, such as those used in many video games and robotics applications.

Jump Point Search Algorithm is very efficient especially in dungeon games or the areas with many obstacles. That's why I used an dungeon theme in the website. For the sake of the mushroom characters who have been crushed for years, a powerful mushroom is chasing Mario on the website. With the JPS algorithm, Mario can escape from the mushroom.

<h2 id="project-architecture">Project Architecture</h3>

<h2 id="results">Results</h3>
<h2 id="conclusion">Conclusion</h3>
