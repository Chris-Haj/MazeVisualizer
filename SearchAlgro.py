
from MazeGen import MazeGen
from Types import Puzzle
import sys


class SearchAlgo:
    DFSStop: bool
    Puzzle: Puzzle
    DFSDict: dict

    def DFSHelper(self, currVer: tuple, end: tuple):

        self.Puzzle.maze[currVer] = 2

        if (self.DFSStop):
            return

        checkOfset = lambda i, j, off_i, off_j: self.Puzzle.maze[i + off_i][j + off_j] == 1
        shape = (self.Puzzle.height, self.Puzzle.width)
        if currVer == end:
            self.DFSStop = True

            while currVer != None:
                self.Puzzle.maze[currVer] = 3
                currVer = self.DfsDict[currVer]

            return
        if currVer[0] > 0 and checkOfset(currVer[0], currVer[1], -1, 0):
            self.DfsDict[(currVer[0] - 1, currVer[1])] = currVer
            self.DFSHelper((currVer[0] - 1, currVer[1]), end)

        if currVer[0] < shape[0] - 1 and checkOfset(currVer[0], currVer[1], 1, 0):
            self.DfsDict[(currVer[0] + 1, currVer[1])] = currVer
            self.DFSHelper((currVer[0] + 1, currVer[1]), end)

        if currVer[1] > 0 and checkOfset(currVer[0], currVer[1], 0, -1):
            self.DfsDict[(currVer[0], currVer[1] - 1)] = currVer
            self.DFSHelper((currVer[0], currVer[1] - 1), end)

        if currVer[1] < shape[1] - 1 and checkOfset(currVer[0], currVer[1], 0, 1):
            self.DfsDict[(currVer[0], currVer[1] + 1)] = currVer
            self.DFSHelper((currVer[0], currVer[1] + 1), end)

    def DFS(self, start: tuple = (-1, -1), end: tuple = (-1, -1)):

        if start == (-1, -1):
            start = self.Puzzle.start
        if end == (-1, -1):
            end = self.Puzzle.end

        self.DFSStop = False
        self.DfsDict = dict()
        self.DfsDict[start] = None
        self.DFS(start, end)

    def BFS(self, start: tuple = (-1, -1), end: tuple = (-1, -1)):

        if start == (-1, -1):
            start = self.Puzzle.start
        if end == (-1, -1):
            end = self.Puzzle.end
        verQueue = [start]
        print(start)
        self.Puzzle.maze[start] = 2
        shape = (self.Puzzle.height, self.Puzzle.width)

        checkOfset = lambda i, j, off_i, off_j: self.Puzzle.maze[i + off_i][j + off_j] == 1
        path = dict()

        def setCell(currVer: tuple, off_i, off_j):
            i, j = currVer
            verQueue.insert(0, (i + off_i, j + off_j))
            self.Puzzle.maze[(i + off_i, j + off_j)] = 2
            path[(i + off_i, j + off_j)] = (i, j)

        path[start] = None

        while len(verQueue) > 0:

            currVer = verQueue.pop()

            if currVer == end:

                while currVer != None:
                    self.Puzzle.maze[currVer] = 3
                    currVer = path[currVer]
                return

            if currVer[0] > 0 and checkOfset(currVer[0], currVer[1], -1, 0):
                setCell(currVer, -1, 0)

            if currVer[0] < shape[0] - 1 and checkOfset(currVer[0], currVer[1], 1, 0):
                setCell(currVer, 1, 0)

            if currVer[1] > 0 and checkOfset(currVer[0], currVer[1], 0, -1):
                setCell(currVer, 0, -1)

            if currVer[1] < shape[1] - 1 and checkOfset(currVer[0], currVer[1], 0, 1):
                setCell(currVer, 0, 1)

    def __init__(self, Puzzle: Puzzle):
        self.DFSStop = False
        self.Puzzle = Puzzle
        self.DfsDict = None
        sys.setrecursionlimit(100000)


if __name__ == "__main__":
    pass
