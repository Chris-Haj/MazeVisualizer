from Types import Puzzle


def isValid(maze, n, m, x, y, res):
    if 0 <= x < n and 0 <= y < m and maze[x][y] == 1 and res[x][y] == 0:
        return True
    return False


def MazeSolve(puzzle, moveX, moveY, position, res, end, screen, pg, clock, NotNeeded):
    x, y = position
    if position == end:
        resCoords = [puzzle.Center(x), puzzle.Center(y)]
        puzzle.addToPath(resCoords)
        return True
    for i in range(4):
        xNew = x + moveX[i]
        yNew = y + moveY[i]

        if isValid(puzzle.maze, puzzle.height, puzzle.width, xNew, yNew, res):
            res[xNew][yNew] = 1
            resCoords = [puzzle.Center(yNew), puzzle.Center(xNew)]
            puzzle.addToPath(resCoords)
            # print(resCoords)

            if MazeSolve(puzzle, moveX, moveY, [xNew, yNew], res, end, screen, pg, clock, NotNeeded):
                return True
            res[xNew][yNew] = 0


    return False


def solveMaze(puzzle: Puzzle, start, screen, pg, clock):
    n, m = puzzle.height, puzzle.width
    res = [[0 for j in range(m)] for i in range(n)]
    res[start[0]][start[1]] = 1
    moveX = [-1, 1, 0, 0]
    moveY = [0, 0, -1, 1]
    NotNeeded = []
    if MazeSolve(puzzle, moveX, moveY, start, res, list(puzzle.end), screen, pg, clock, NotNeeded):
        for coords in NotNeeded:
            print(coords, type(coords))
            puzzle.path.pop(puzzle.path.index(coords))
        for path in puzzle.path:
            screen.blit(path[0].surf, path[0].rect)
            clock.tick(15)
            pg.display.update()
    else:
        print("No sol")

