import random

class node():
    def __init__(self, x, y, wid, hei, offset):
        self.x = x
        self.y = y
        self.wid = wid
        self.hei = hei
        self.f = 0
        self.g = 0
        self.h = 0
        self.start = None
        self.finish = None
        self.offset = offset
        self.neighbors = []
        self.prev = None
        if random.uniform(0, 1) < 0.25:
            self.obstacle = True
        else:
            self.obstacle = False
        
    def show(self, col):
        noStroke()
        fill(col)
        if self.obstacle:
            fill(0)
        # rect(self.x*self.wid+self.offset,
        #      self.y*self.hei+self.offset,
        #      self.wid, self.hei)
        ellipse(self.x*self.wid+self.offset,
             self.y*self.hei+self.offset,
             self.wid-2, self.hei-2)
        
    def addNeighbors(self, grid, cols, rows):
        if self.x < cols-1:
            self.neighbors.append(grid[self.x+1][self.y])
        if self.x > 0: 
            self.neighbors.append(grid[self.x-1][self.y])
        if self.y < rows-1:
            self.neighbors.append(grid[self.x][self.y+1])
        if self.y > 0:
            self.neighbors.append(grid[self.x][self.y-1])
    
