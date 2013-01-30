##A* (star) performs better than the algorithm where we expand every node,
##A* uses a heuristic function, which an optimistic guess of how far we are
##from the goal, eg h(x,y) <= distance of goal from x,y - for any x,y in our
##grid maze, so we take the case when there are no obstacles (when its easy to
##know the distance from goal d=x+y if we cannot move diagonal,
##else d=sqrt(x^2 + y^2)=euclidean distance, used in case of free motion
##like car) to generate our heuristic function, the heuristic function doesn't
##have to be accurate, its an optimistic guess. If we set all h(x,y) to be zero
##then we go to the worst case and it work same as our expand algorithm
##So in A* we calculate a f-value which is f = g+h(x,y), where g is same as
##our previous algorithm, and now when we expand we pick the element with
##the lowest f-value instead of g, its based on that we try to expand the node
##which would have had the shortest path in ideal case, so f value for the
##ideal nodes will be lower

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]

heuristic = [[9, 8, 7, 6, 5, 4],
            [8, 7, 6, 5, 4, 3],
            [7, 6, 5, 4, 3, 2],
            [6, 5, 4, 3, 2, 1],
            [5, 4, 3, 2, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost = 1

# ----------------------------------------
# modify code below
# ----------------------------------------

def search():
    visited= [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    visited[init[0]][init[1]] = 1

    expand = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    action = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]


    x = init[0]
    y = init[1]
    g = 0
    f = g + heuristic[x][y]
    open_c = [[f, g, x, y]] #list of cells not visited

    found = False  # flag that is set when search is complete
    resign = False # flag set if we can't find the goal
    count = 0
    
    while not found and not resign:
        if len(open_c) == 0:
            resign = True
            return "Fail"
        else:
            open_c.sort()#sort in increasing order and then reverse for pop to work
            open_c.reverse()#f/g-value has to be the first if we want to sort by it
            next_c = open_c.pop() #pops the last element, so we reverse earlier
            x = next_c[2]
            y = next_c[3]
            g = next_c[1]
            expand[x][y] = count
            count += 1
            #print next
            if x == goal[0] and y == goal[1]:
                found = True
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                        if visited[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            f2 = g2 + heuristic[x2][y2]
                            open_c.append([f2, g2, x2, y2])
                            visited[x2][y2] = 1
    for i in range(len(expand)):
        print expand[i]
    return expand 

search()

