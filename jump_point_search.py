import itertools, heapq

# c2huc2hu / jps
# Define some constants representing the things that can be in a field.
OBSTACLE = -10
DESTINATION = -2
UNINITIALIZED = -1

DEBUG = False  
VISUAL = True
expanded = [[False for j in range(15)] for i in range(20)]  
visited = [[False for j in range(15)] for i in range(20)]

class HeapTree():
    def __init__(self):
        self.pq = []                         # list of entries arranged in a heap
        self.counter = itertools.count()     # unique sequence count

    def add_task(self, task, priority=0):
        'Add a new task'
        count = next(self.counter)
        entry = [priority, count, task]
        heapq.heappush(self.pq, entry)

    def pop_task(self):
        'Remove and return the lowest priority task. Raise KeyError if empty.'
        while self.pq:
            priority, count, task = heapq.heappop(self.pq)
            return task
        raise KeyError('pop from an empty priority queue')

    def empty(self):
        return len(self.pq) == 0

def generate_field(terrain, walkable_fcn, pad=False) -> list[list[int]]:
    """
    Generate a field from any format as long as a function is provided to determine whether a cell is walkable. 

    :param terrain: a 2d rectangular iterable somehow representing the terrain.
    param walkable_fcn : a function that takes a a cell from terrain as an argument and returns whether that cell can be walked on.
    param pad : if true, this function sets the outermost layer of the map to obstacles. if not, the function does nothing.
    
    Returns: the field
    """
    field = [[UNINITIALIZED if walkable_fcn(j) else OBSTACLE for j in i] for i in terrain]
    if pad:
        pad_field(field)
    return field 
        
def pad_field(field):
    """
    Fill the outer border of a field with obstacles
    Parameters
    field - a 2d rectangular array with obstacles.
    Returns:
    None
    """
    for i in range(len(field)):
        field[i][0] = OBSTACLE
        field[i][-1] = OBSTACLE
    for j in range(len(field[0])):
        field[0][j] = OBSTACLE
        field[-1][j] = OBSTACLE

def jump_point_search(field, start_x, start_y, end_x, end_y):
    """
    Run a jump point search on a field with obstacles.
    
    Parameters
    field            - 2d array representing the cost to get to that node.
    start_x, start_y - the x, y coordinates of the starting position (must be ints)
    end_x, end_y     - the x, y coordinates of the destination (must be ints)
    Return:
    a list of tuples corresponding to the jump points. drawing straight lines betwen them gives the path.
    OR
    [] if no path is found. 
    """
    global expanded, visited
    if VISUAL:
        expanded = [[False for j in range(len(field[0]))] for i in range(len(field))]  
        visited = [[False for j in range(len(field[0]))] for i in range(len(field))]  
    
    # handle obvious exception cases: either start or end is unreachable
    if field[start_x][start_y] == OBSTACLE:
        raise ValueError("No path exists: the start node is not walkable")
    if field[end_x][end_y] == OBSTACLE:
        raise ValueError("No path exists: the end node is not walkable")

    class FoundPath(Exception):
        """ Raise this when you found a path. it's not really an error,
        but I need to stop the program and pass it up to the real function"""
        pass

    def queue_jumppoint(node):
        """
        Add a jump point to the priority queue to be searched later. The priority is the minimum possible number of steps to the destination. 
        Also check whether the search is finished.
        Parameters
        pq - a priority queue for the jump point search
        node - 2-tuple with the coordinates of a point to add.
        Return
        None
        """
        if node is not None:
            pq.add_task (node, field [node[0]] [node[1]] + max(abs(node[0] - end_x), abs(node[1] - end_y)))

            
    def _jps_explore_diagonal (startX, startY, directionX, directionY):
        """
        Explores field along the diagonal direction for JPS, starting at point (startX, startY)
        Parameters
        startX, startY - the coordinates to start exploring from. 
        directionX, directionY - an element from: {(1, 1), (-1, 1), (-1, -1), (1, -1)} corresponding to the x and y directions respectively. 
        Return
        A 2-tuple containing the coordinates of the jump point if it found one
        None if no jumppoint was found. 
        """
        current_x, current_y = startX, startY #indices of current cell.
        current_cost = field[startX][startY]

        while (True):
            current_x += directionX
            current_y += directionY
            current_cost += 2**(1/2)

            if field[current_x][current_y] == UNINITIALIZED:
                field[current_x][current_y] = current_cost
                sources[current_x][current_y] = startX, startY
                if VISUAL:
                    visited[current_x][current_y] = True
            elif current_x == end_x and current_y == end_y:  # destination found
                field[current_x][current_y] = current_cost
                sources[current_x][current_y] = startX, startY
                if VISUAL:
                    visited[current_x][current_y] = True
                raise FoundPath()
            else: #collided with an obstacle. We are done. 
                return None

            # If a jump point is found, 
            if field[current_x + directionX][current_y] == OBSTACLE and field[current_x + directionX][current_y + directionY] != OBSTACLE:
                return (current_x, current_y)
            else: #otherwise, extend a horizontal "tendril" to probe the field.
                queue_jumppoint(_jps_explore_cardinal (current_x, current_y, directionX, 0))

            if field[current_x][current_y + directionY] == OBSTACLE and field[current_x + directionX][current_y + directionY] != OBSTACLE:
                return (current_x, current_y)
            else: #extend a vertical search to look for anything 
                queue_jumppoint(_jps_explore_cardinal (current_x, current_y, 0, directionY))

    def _jps_explore_cardinal (startX, startY, directionX, directionY):
        """
        Explores field along a cardinal direction for JPS (north/east/south/west), starting at point (startX, startY)
        Parameters
        startX, startY - the coordinates to start exploring from. 
        directionX, directionY - an element from: {(1, 1), (-1, 1), (-1, -1), (1, -1)} corresponding to the x and y directions respectively. 
        Result: 
        A 2-tuple containing the coordinates of the jump point if it found one
        None if no jumppoint was found.
        """
        current_x, current_y = startX, startY #indices of current cell. 
        current_cost = field [startX] [startY]

        while (True):
            current_x += directionX
            current_y += directionY
            current_cost += 1

            if field [current_x] [current_y] == UNINITIALIZED:
                field [current_x][current_y] = current_cost
                sources [current_x] [current_y] = startX, startY
                if VISUAL:
                    visited[current_x][current_y] = True  
            elif current_x == end_x and current_y == end_y:  # destination found
                field [current_x][current_y] = current_cost
                sources [current_x] [current_y] = startX, startY
                if VISUAL:
                    visited[current_x][current_y] = True
                raise FoundPath()
            else: #collided with an obstacle or previously explored part. We are done. 
                return None

            #check neighbouring cells, i.e. check if current_x, current_y is a jump point. 
            if directionX == 0: 
                if field [current_x + 1] [current_y] == OBSTACLE and field [current_x + 1] [current_y + directionY] != OBSTACLE:
                    return current_x, current_y
                if field [current_x - 1] [current_y] == OBSTACLE and field [current_x - 1] [current_y + directionY] != OBSTACLE:
                    return current_x, current_y
            elif directionY == 0:
                if field [current_x] [current_y + 1] == OBSTACLE and field [current_x + directionX] [current_y + 1] != OBSTACLE:
                    return current_x, current_y
                if field [current_x] [current_y - 1] == OBSTACLE and field [current_x + directionX] [current_y - 1] != OBSTACLE:
                    return current_x, current_y

    # MAIN JPS FUNCTION
    field = [[j for j in i] for i in field]  # this takes less time than deep copying. 

    # Initialize some arrays and certain elements. 
    sources = [[(None, None) for i in field[0]] for j in field]  # the jump-point predecessor to each point.
    field [start_x] [start_y] = 0
    field [end_x] [end_y] = DESTINATION

    pq = HeapTree()
    queue_jumppoint((start_x, start_y))

    # Main loop: iterate through the queue
    while (not pq.empty()):
        pX, pY = pq.pop_task()

        if VISUAL:
            expanded[pX][pY] = True 
        
        try:
            queue_jumppoint(_jps_explore_cardinal (pX, pY, 1, 0))
            queue_jumppoint(_jps_explore_cardinal (pX, pY, -1, 0))
            queue_jumppoint(_jps_explore_cardinal (pX, pY, 0, 1))
            queue_jumppoint(_jps_explore_cardinal (pX, pY, 0, -1))

            queue_jumppoint(_jps_explore_diagonal (pX, pY, 1, 1))
            queue_jumppoint(_jps_explore_diagonal (pX, pY, 1, -1))
            queue_jumppoint(_jps_explore_diagonal (pX, pY, -1, 1))
            queue_jumppoint(_jps_explore_diagonal (pX, pY, -1, -1))
        except FoundPath:
            return _get_path(sources, start_x, start_y, end_x, end_y)

    raise ValueError("No path is found")
    #end of jps
    

def _get_path(sources, start_x, start_y, end_x, end_y):
    """
    Reconstruct the path from the source information as given by jps(...).
    Parameters
    sources          - a 2d array of the predecessor to each node
    start_x, start_y - the x, y coordinates of the starting position
    end_x, end_y     - the x, y coordinates of the destination
    
    Return
    a list of jump points as 2-tuples (coordinates) starting from the start node and finishing at the end node.
    """
    result = []
    current_x, current_y = end_x, end_y
    
    while current_x != start_x or current_y != start_y:
        result.append((current_x, current_y))
        current_x, current_y = sources[current_x][current_y]
    result.reverse()
    return [(start_x, start_y)] + result

def _signum(n):
    return 1 if n > 0 else -1 if n < 0 else 0

def get_full_path(path):
    """
    Generates the full path from a list of jump points. Assumes that you moved in only one direction between
    jump points.
    Parameters
    path - a path generated by get_path
    Return
    a list of 2-tuples (coordinates) starting from the start node and finishing at the end node.
    """

    if path == []:
        return []
    
    current_x, current_y = path[0]
    result = [(current_x, current_y)]
    for i in range(len(path) - 1):
        while current_x != path[i + 1][0] or current_y != path[i + 1][1]:
            current_x += _signum(path[i + 1][0] - path[i][0])
            current_y += _signum(path[i + 1][1] - path[i][1])
            result.append([current_x, current_y])
    return result

def drawGrid (field):
    """
    Represent the field as a grid. Pretty much prints out the 2d array, but prints obstacles nicely.
    Parameters
    field - a 2d array with the obstacles and whatever else happens to be in the field. 
    Return
    None
    """
    print ("=======================================")
    for i in field: 
        for j in i:
            if j == OBSTACLE:
                print ("###", end=" ")
            else:
                print ("{:<3}".format(j), end=" ") 
        print("")

# Turn visual and debug modes on/ off
def set_visual(val):
    global VISUAL
    VISUAL = val
def set_debug(val):
    global DEBUG
    DEBUG = val    