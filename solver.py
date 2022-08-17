def isSafe(maze, x, y, n, m) -> bool:
    if 0 <= x < n and 0 <= y < m and maze[x][y] == 1:
        return True

    return False


def solveMaze(maze, n, m) -> bool:
    sol = [[0 for j in range(n)] for i in range(m)]
    if not solveMazeUtil(maze, 0, 0, sol):
        print("Solution doesn't exist")
        return False
    return True


def solveMazeUtil(maze, x, y, sol, n, m) -> bool:
    if x == n - 1 and y == m - 1 and maze[x][y] == 1:
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
