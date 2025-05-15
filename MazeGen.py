from array import ArrayType
import numpy as np
import random as rn

class MazeGen:
    
    Shape:tuple
    Board:ArrayType
    startPoint:tuple
    endPoint:tuple
    
    def __init__(self,height:int,width:int = 0,startPoint:tuple = (-1,-1)):
        if width == 0:
            width = height
        if (startPoint[0] == -1 or startPoint[1] == -1):
            startPoint = (rn.randint(0, height - 1), rn.randint(0, width - 1))
        self.Shape = (height, width)
        self.startPoint = startPoint
        self.Board = np.zeros(self.Shape, dtype=np.uint8)
        self.genMaze()
        self.createStartEnd()

    def genMaze(self):
        verStack = []
        checkOfset = lambda i,j,off_i,off_j : self.Board[i+off_i][j+off_j] == 0
        
        verStack.append(self.startPoint)
        visted = 1
        allVertexCount = int(self.Shape[0] * self.Shape[1] / 4)

        while (visted < allVertexCount):

            neighborList = []
            nDir = []
            currVer = verStack[len(verStack) - 1]
            self.Board[currVer] = 1

            # up check
            if (currVer[0] > 1 and checkOfset(currVer[0], currVer[1], -2, 0)):
                neighborList.append((currVer[0] - 2, currVer[1]))
                nDir.append("u")
            # down check
            if (currVer[0] < self.Shape[0] - 2 and checkOfset(currVer[0], currVer[1], +2, 0)):
                neighborList.append((currVer[0] + 2, currVer[1]))
                nDir.append("d")

            # left check
            if (currVer[1] > 1 and checkOfset(currVer[0], currVer[1], 0, -2)):
                neighborList.append((currVer[0], currVer[1] - 2))
                nDir.append("l")

            # right check
            if (currVer[1] < self.Shape[1] - 2 and checkOfset(currVer[0], currVer[1], 0, +2)):
                neighborList.append((currVer[0], currVer[1] + 2))
                nDir.append("r")
            if len(nDir) == 0:
                verStack.pop()
            else:
                nextVerindex = rn.randint(0, len(nDir) - 1)
                hoShift = 0
                veShift = 0

                if "r" in nDir[nextVerindex]:
                    hoShift = 1
                if "l" in nDir[nextVerindex]:
                    hoShift = -1
                if "u" in nDir[nextVerindex]:
                    veShift = -1
                if "d" in nDir[nextVerindex]:
                    veShift = 1
                self.Board[currVer[0] + veShift][currVer[1] + hoShift] = 1

                verStack.append(neighborList[nextVerindex])
                visted+=1
        left = 0
        right = 0
        up = 0
        down = 0

        for i in range(self.Shape[0]):
            if (self.Board[i][0] == 1):
                left = 1
                break
        for i in range(self.Shape[0]):
            if (self.Board[i][self.Shape[1] - 1] == 1):
                right = 1
                break
        for i in range(self.Shape[1]):
            if (self.Board[0][i] == 1):
                up = 1
                break
        for i in range(self.Shape[1]):
            if (self.Board[self.Shape[0] - 1][i] == 1):
                down = 1
                break

        self.Board = np.pad(self.Board, ((up, down), (left, right)), mode='constant', constant_values=[0])
        self.Shape = self.Board.shape

    def createStartEnd(self):
        
        ind_xs = rn.randint(0,self.Shape[0]-1)
        ind_xe = rn.randint(0,self.Shape[0]-1)
        while self.Board[ind_xs][1] == 0:
            ind_xs = rn.randint(0,self.Shape[0]-1)
        while self.Board[ind_xe][self.Shape[1]-2] == 0:
            ind_xe = rn.randint(0,self.Shape[0]-1)

        self.Board[ind_xs][0] = 1
        self.Board[ind_xe][self.Shape[1]-1] = 1 

        self.startPoint = (ind_xs, 0)
        self.endPoint = (ind_xe, self.Shape[1] - 1)

    def __str__(self) -> str:

        string = ""
        for i in range(self.Shape[0]):
            for j in range(self.Shape[1]):
                if (self.Board[i][j] == 1):
                    string += "  "
                elif self.Board[i][j] == 2:
                    string += "  "
                elif self.Board[i][j] == 3:
                    string += "P "
                elif self.Board[i][j] == 0:
                    string += "# "
                    
            string += "\n"

        return string