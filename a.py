# Randomly generate obstacles on a field, and display the output using pygame.


from jump_point_search import *
import random

DENSITY = 5  # Percentage of the field that is filled. 

set_visual(True)
set_debug(True)

DEBUG = True

if DEBUG:
    import cProfile, time
    pr = cProfile.Profile()
    t = time.time()

x_field = [[0]*20 for i in range(20)]
for i in range(len(x_field)):
    for j in range(len(x_field[0])):
        if i == 0 or i == 19 or j == 0 or j == 19:
            x_field[i][j] = -10
        else:
            x_field[i][j] = -1

raw_field = [[random.randint(0, 15) for i in range(20)] for j in range(20)]
#field = generate_field(x_field, (lambda cell: True if cell > DENSITY else False), True)
field = x_field
field[1][1] = UNINITIALIZED  # guarantee that the end is reachable
field[15][15] = UNINITIALIZED


if DEBUG:
    print("took ", time.time() - t, " to generate field")
    t = time.time()
    pr.enable() # start the profiler
    
path = jump_point_search(field, 1, 1, 5, 5)
path = get_full_path(path)

if DEBUG:
    pr.disable()
    print("took ", (time.time() - t), " to do search")
    t = time.time()
    print("full long path: ", path)
    pr.print_stats() 

if VISUAL:
    try:
        drawGrid(field)
    except ImportError as err:
        print("You don't have pygame. Cannot display large test. ", err)
else:
    print("Visual is turned off") 