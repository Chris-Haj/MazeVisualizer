
def isValid(maze, n, m, x, y, res):
    if 0 <= x < n and 0 <= y < m and maze[x][y] == 1 and res[x][y] == 0:
        return True
    return False


def MazeSolve(maze, n, m, moveX, moveY, position, res, end):
    x, y = position
    if position == end:
        return True
    for i in range(4):
        xNew = x + moveX[i]
        yNew = y + moveY[i]

        if isValid(maze, n, m, xNew, yNew, res):
            res[xNew][yNew] = 2
            if MazeSolve(maze, n, m, moveX, moveY, [xNew, yNew], res, end):
                return True
            res[xNew][yNew] = 0
    return False


def solveMaze(maze, n, m, start, end):
    res = [[0 for j in range(m)] for i in range(n)]
    res[start[0]][start[1]] = 1
    moveX = [-1, 1, 0, 0]
    moveY = [0, 0, -1, 1]

    if MazeSolve(maze, n, m, moveX, moveY, start, res, end):
        return res
    else:
        print("No sol")


if __name__ == '__main__':
    maze = [[1, 0, 0, 0],
            [1, 1, 0, 1],
            [0, 1, 1, 1],
            [1, 0, 1, 1],
            [1, 0, 1, 1]]
    n = len(maze)
    m = len(maze[0])
    print(n,m)
    start = [0, 0]
    end = [n - 1, m - 1]
    res = solveMaze(maze, n, m, start, end)

