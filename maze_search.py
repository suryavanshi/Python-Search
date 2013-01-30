# ----------
# User Instructions:
# 
# Define a function, search() that takes no input
# and returns a list
# in the form of [optimal path length, x, y]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1] # Make sure that the goal definition stays in the function.

delta = [[-1, 0 ], # go up
        [ 0, -1], # go left
        [ 1, 0 ], # go down
        [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost = 1

def search():
    # ----------------------------------------
    # insert code here and make sure it returns the appropriate result
    # ----------------------------------------
    visited = [[0 for row in range(len(grid[0]))] for col in range(len(grid[0])-1)]
    visited[init[0]][init[1]] = 1 #0 means open, 1 means closed/visited
    x = init[0]
    y = init[0]
    g=0
    open_c = [[g,x,y]] #list of cells not visited
    found = False #becomes true when the gaol is found
    resign = False #set true if we can't find a path
    cnt = 0
    print "Goal=",goal
    while (found == False and resign == False):
        cnt = cnt+1
        if len(open_c) == 0:
            resign = True
            print "Search Failed!", cnt
        else :
            open_c.sort()#sort in increasing order and then reverse for pop to work
            open_c.reverse() #g-value has to be the first if we want to sort by it
            next_c = open_c.pop() #pops the last element, so we reverse earlier
            x = next_c[1]
            y = next_c[2]
            g = next_c[0]
            #print "next = ",next_c
            if (x == goal[0] and y==goal[1]):
                found = True
                print "Found Goal!!-"
                path = next_c
                print next_c
            else:
                for i in range(len(delta)): #len(delta) is the number of movements-up,down,left,right
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if (x2>=0 and x2 < len(grid) and y2>=0 and y2 <= len(grid[0])-1):
                        if (visited[x2][y2] == 0 and grid[x2][y2] == 0):
                            g2 = g + cost
                            open_c.append([g2,x2,y2])
                            #print "append",cnt,[g2,x2,y2],open_c
                            visited[x2][y2] = 1
            
    
    return path
         
        
    

search()
