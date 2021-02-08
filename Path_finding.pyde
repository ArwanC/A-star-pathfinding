from Node import node
from Environment import environment
import time

offset = 100
side = 20

'''
A* path finding algorithm

> 'Space' - Randomize grid with 25% obstacle probability
> 'Return' - Start path finding algorithm
> Right-click - Set finish zone
> Left-click - Set starting zone
> Mouse-drag - Add obstacles
> 'e' - Toggle between adding obstacle and removing obstacles
> 'r' - Reset grid to blank

'''

def setup():
    global env
    size(700, 700)
    frameRate(30000)
    
    env = environment(int((height-2*offset)/side), int((width-2*offset)/side), side, side)
    print("Launch")

    for i in range(env.cols):
        for j in range(env.rows):
            env.grid[i][j] = node(i, j, env.w, env.h, offset)
    for i in range(env.cols):
        for j in range(env.rows):
            env.grid[i][j].addNeighbors(env.grid, env.cols, env.rows)
    env.reset(False)

def draw():
    if env.findPath:
        if env.openSet:
            best = 0
            for i in range(len(env.openSet)):
                if env.openSet[i].f < env.openSet[best].f:
                    best = i
            env.current = env.openSet[best]
            if env.current == env.finish:
                print("Done")
                save("mazes/"+time.strftime("%Y%m%d-%H%M%S")+".tga")
                env.findPath = False
                env.succeeded = True
            env.openSet.remove(env.current)
            env.closedSet.append(env.current)
            
            neighbors = env.current.neighbors
            for nei in neighbors:
                if nei not in env.closedSet and not nei.obstacle:
                    tempG = env.current.g + 1
                    if nei in env.openSet:
                        if tempG<nei.g:
                            nei.g = tempG
                    else:
                        nei.g = tempG
                        env.openSet.append(nei)
                        
                    nei.h = heuristic(nei, env.finish)
                    nei.f = nei.g + nei.h
                    nei.prev = env.current
        else:
            print("No Solutions")
            save("mazes/"+time.strftime("%Y%m%d-%H%M%S")+".tga")
            env.findPath = False
            env.failed = True
    fill(255)
    stroke(0)
    strokeWeight(side/3);
    background(255)
    rect(offset-side, offset-side, height-2*offset+side, width-2*offset+side, 10)
    env.refresh_grid()
    
    if env.findPath or env.succeeded:
        path = []
        temp = env.current
        path.append(temp)
        while temp.prev:
            path.append(temp.prev)
            temp = temp.prev
        for elem in path:
            elem.show("#F24957")

            
def heuristic(node1, node2):
    d1 = abs(node1.x - node2.x)
    d2 = abs(node1.y - node2.y)
    return d1+d2

def mouseDragged():
    mouse_row = ((mouseY-offset)/side)
    mouse_col = ((mouseX-offset)/side)
    if 0 <= mouse_row < (height-2*offset)/side and 0 <= mouse_col < (width-2*offset)/side:
        if env.drawing:
            env.grid[mouse_col][mouse_row].obstacle = True
        else:
            env.grid[mouse_col][mouse_row].obstacle = False

def mousePressed():
    mouse_row = ((mouseY-offset)/side)
    mouse_col = ((mouseX-offset)/side)
    if 0 <= mouse_row < (height-2*offset)/side and 0 <= mouse_col < (width-2*offset)/side:
        if (mouseButton == LEFT):
            env.start = env.grid[mouse_col][mouse_row]
        elif (mouseButton == RIGHT):
            env.finish = env.grid[mouse_col][mouse_row]
      
        
def keyPressed():
    loop()
    
    if key == 'e':
        env.drawing = not env.drawing
    if key == 'r':
        env.reset()
        print("Erase grid")
        for i in range(env.cols):
            for j in range(env.rows):
                env.grid[i][j].obstacle = False
    if key == ' ':
        env.reset()
        print("Randomize grid")
        for i in range(env.cols):
            for j in range(env.rows):
                env.grid[i][j] = node(i, j, env.w, env.h, offset)
        for i in range(env.cols):
            for j in range(env.rows):
                env.grid[i][j].addNeighbors(env.grid, env.cols, env.rows)
        
    if key == '\n':
        env.reset(False)
        print("Starting path finding")
        env.findPath = True
        env.failed = False
