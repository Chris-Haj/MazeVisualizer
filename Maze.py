N = 5


class Puzzle:
    def __init__(self):
        self.start = [0, 0]
        self.end = [4, 0]
        self.maze = [['S', 1, 1, 1, 1],
                     [0, 0, 0, 0, 1],
                     [1, 1, 1, 0, 1],
                     [1, 0, 1, 0, 1],
                     ['E', 0, 1, 1, 1]]


def print_maze(self) -> None:
    for i in range(len(self) + 2):
        print("--", end="")
    print("")
    for i in range(len(self)):
        print("| ", end="")
        for j in range(len(self[i])):
            print(self[i][j], end=" ")
        if i < (len(self)):
            print("|")
        else:
            print("|", end="")

    for i in range(len(self) + 2):
        print("--", end="")
    print("")


def isSafe(maze, x, y) -> bool:
    if x >= 0 and x < N and y >= 0 and y < N and maze[x][y] == 1:
        return True

    return False


def solveMaze(maze) -> bool:
    sol = [[0 for j in range(N)] for i in range(N)]
    if solveMazeUtil(maze, 0, 0, sol) == False:
        print("Solution doesn't exist")
        return False
    print_maze(maze)
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


def main():
    puzzle = Puzzle()
    solveMaze(puzzle.maze)


if __name__ == '__main__':
    main()
