class environment():
    def __init__(self, rows, cols, w, h):
        self.rows = rows
        self.cols = cols
        self.grid = [[0 for i in range(rows)] for j in range(cols)] 
        self.openSet = []
        self.closedSet = []
        self.path = []
        self.start = None
        self.finish = None
        self.w = w
        self.h = h
        self.findPath = False
        self.failed = False
        self.succeeded = False
        self.drawing = True
            
    def reset(self, also_finish=True):
        self.findPath = False
        self.succeeded = False
        self.openSet = []
        self.closedSet = []
        self.failed = False
        # if also_finish:
        self.start = self.grid[0][0]
        self.finish = self.grid[self.cols-1][self.rows -1]
        self.finish.obstacle = False
        self.start.obstacle = False
        self.openSet.append(self.start)
        self.path = []
        self.refresh_grid()
        self.drawing = True
        self.current = None
        
    def refresh_grid(self):
        for i in range(self.cols):
            for j in range(self.rows):
                self.grid[i][j].show(color(255))
        if self.finish:
            self.finish.show("#F24957")
        if self.start:
            self.start.show("#230BBF")
        for elem in self.closedSet:
            elem.show("#A0D3F2")
        # if self.openSet:
        #     if self.openSet[0] != None:
        for elem in self.openSet:
            elem.show("#230BBF")
            
