
from array import ArrayType
from re import T
import numpy as np
import random as rn

class Maze:
    
    Shape:tuple
    Board:ArrayType

    def __init__(self,height:int,width:int = 0):
        if width == 0:
            width = height
        self.Shape = (height,width)
        self.Board = np.ones(self.Shape,dtype=np.uint8)
        self.genMaze()
        
    def genMaze(self):
        pointsList = []
        for i in range(self.Shape[0]*15):
            pointsList.append((rn.randint(1,self.Shape[0]-2),rn.randint(1,self.Shape[1]-2)))
        self._connectPointList(pointsList)
        self.createEndAndStart()

    def _moveStep(self,startP:tuple,steps:int,Dir:str)->tuple:
        
        if( self.Shape[0] <= startP[0] or startP[0] <= 0 ):
            return startP
        if( self.Shape[1] <= startP[1]  or startP[1] <= 0 ):
            return startP
        if steps == 0:
            return (startP)
        x_movement = 0
        y_movement = 0
        ver = False

        if "D" in Dir:
            y_movement += steps
            ver = True
        if "L" in Dir:
            x_movement -= steps
        if "R" in Dir:
            x_movement += steps
        if "U" in Dir:
            y_movement -= steps
            ver = True
        y_index = y_movement+startP[0]
        x_index = x_movement+startP[1]
        
        
        if(y_index >= self.Shape[0]-1):
            y_index = self.Shape[0]-2
        elif(y_index <= 0):
            y_index =1
        
        if(x_index >= self.Shape[1]-1):
            x_index = self.Shape[1]-2
        elif(x_index <= 0):
            x_index =1
        
        i = startP[0]
        j = startP[1]
        while(i != y_index or j != x_index):
            
            if(y_index > i):
                i += 1
            elif(y_index < i):
                i -= 1
            if(x_index > j):
                j += 1
            elif(x_index < j):
                j -= 1
            

            sum = 1.1*(self.Board[i+1][j+1] + self.Board[i-1][j-1] +self.Board[i-1][j+1]+ self.Board[i+1][j-1])+ 1.1*(self.Board[i+1][j] + self.Board[i][j+1] + self.Board[i-1][j] + self.Board[i][j-1])
            if(sum >= 5.4):
                self.Board[i][j] = 0 
                
        return (y_index,x_index)

    def _connectPoints(self,pointA:tuple,pointB:tuple,prioraty:bool = False):

        verStep = np.abs(pointA[0] - pointB[0])
        horStep = np.abs(pointA[1] - pointB[1])

        
        verDir = ""
        horDir = ""
        if(pointA[0] < pointB[0]):
            verDir += 'D'
        else:
            verDir += 'U'

        if(pointA[1] < pointB[1]):

            horDir += "R"
        else:
            horDir += "L"
        if prioraty:

            nextp = self._moveStep(pointA,horStep,horDir)
            self._moveStep(nextp,verStep,verDir)
        else:
            
            nextp = self._moveStep(pointA,verStep,verDir)
            self._moveStep(nextp,horStep,horDir) 
        
    def _connectPointList(self,pointList:list):
        for i in range(len(pointList)-1):
            self._connectPoints(pointList[i],pointList[i+1],rn.randint(0,1))

    def createEndAndStart(self):
        
        for i in range(self.Shape[1]):
            x = rn.randint(0,self.Shape[0]-1)
            j= 0
            while self.Board[x][i] != 0 and j < 20:
                j+=1
                x = rn.randint(0,self.Shape[0]-1)
            self.Board[x][i] = 0
        
        # for i in range(self.Shape[0]):
        #     if(self.Board[i][1] == 0):
        #         self.Board[i][0] = 0
        #         break

        # for i in range(self.Shape[0]):
        #     if(self.Board[i][self.Shape[1]-2] == 0):
        #         self.Board[i][self.Shape[1]-1] = 0
        #         break

    def __str__(self) -> str:
        
        string = ""
        for i in range(self.Shape[0]):
            for j in range(self.Shape[1]):
                if(self.Board[i][j] == 0):
                    string += "  "
                else:
                    string += "# "
            string += "\n"

        return string


