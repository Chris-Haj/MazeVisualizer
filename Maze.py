N = 6


class Puzzle:
    def __init__(self):
        self.start = [0, 0]
        self.end = [5, 0]
        self.maze = [[1, 1, 1, 1, 1, 0],
                     [0, 0, 0, 0, 1, 1],
                     [1, 1, 1, 0, 0, 1],
                     [1, 0, 1, 0, 1, 1],
                     [1, 0, 1, 0, 1, 0],
                     [1, 0, 1, 1, 1, 0]]


def isSafe(maze, x, y) -> bool:
    if 0 <= x < N and 0 <= y < N and maze[x][y] == 1:
        return True

    return False


def solveMaze(maze) -> bool:
    sol = [[0 for j in range(N)] for i in range(N)]
    if not solveMazeUtil(maze, 0, 0, sol):
        print("Solution doesn't exist")
        return False
    return True


def solveMazeUtil(maze, x, y, sol) -> bool:
    if x == N - 1 and y == N - 1 and maze[x][y] == 1:
        sol[x][y] = 1
        return True

    # Check if maze[x][y] is valid
    if isSafe(maze, x, y):

        if sol[x][y] == 1:
            return False

        sol[x][y] = 1

        if solveMazeUtil(maze, x + 1, y, sol):
            return True

        if solveMazeUtil(maze, x, y + 1, sol):
            return True

        if solveMazeUtil(maze, x - 1, y, sol):
            return True

        if solveMazeUtil(maze, x, y - 1, sol):
            return True

        sol[x][y] = 0
        return False



