
class Bot:
    def __init__(self, grid):
        '''Constructor to set initial grid'''
        self.grid = grid

    def toHex(self, x):
        ''' A function to convert int to hex'''
        return hex(x)

    def toInt(self, x):
        '''A function to convert hex to int'''
        return int(x,16)

    def traverse(self):
        '''With the help of trace matrix storing minimum distance for i,j location'''
        n,m = len(self.grid), len(self.grid[0])
        trace = [[0 for i in range(m)] for j in range(n)]
        trace[0][0] = self.toInt(self.grid[0][0])
        for i in range(1,n):
            trace[i][0] = trace[i-1][0] + self.toInt(self.grid[i][0])
        for j in range(1,m):
            trace[0][j] = trace[0][j-1] + self.toInt(self.grid[0][j-1])

        for i in range(1,n):
            for j in range(1,m):
                trace[i][j] = self.toInt(self.grid[i][j]) + min(trace[i-1][j], trace[i][j-1])
        self.pathFinder(trace, n, m)
        return str(self.toHex(trace[n-1][m-1])).lstrip("0x")

    def pathFinder(self, trace, n, m):
        '''Traversing trace matrix to find path direction on each location'''
        i, j = 0, 0
        while i<n-1 and j<m-1:
            if trace[i+1][j] < trace[i][j+1]:
                self.moveDown()
                i += 1
            else:
                self.moveRight()
                j += 1
        while i < n-1:
            self.moveDown()
            i += 1
        while j < m-1:
            self.moveRight()
            j += 1
        print

    def moveRight(self):
        print "r",

    def moveDown(self):
        print "d",

# Driver Program
# if __name__ == '__main__':
#     grid = []
#     grid.append(["46B", "E59", "EA", "C1F", "45E", "63"])
#     grid.append(["899", "FFF", "926", "7AD", "C4E", "FFF"])
#     grid.append(["E2E", "323", "6D2", "976", "83F", "C96"])
#     grid.append(["9E9", "A8B", "9C1", "461", "F74", "D05"])
#     grid.append(["EDD", "E94", "5F4", "D1D", "D03", "DE3"])
#     grid.append(["89", "925", "CF9", "CA0", "F18", "4D2"])
#     b = Bot(grid)
#     print b.traverse()

