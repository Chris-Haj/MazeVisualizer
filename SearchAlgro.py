from ast import main
import os
from turtle import shape
import numpy as np
from tkinter import *
import time
from MazeGen import MazeGen
import random as rn 
import sys


class SearchAlgo:

    DfsStop:bool
    Puzzle:MazeGen
    DfsDict : dict

    def DfsHelper(self,currVer:tuple,endPoint:tuple):

        self.Puzzle.Board[currVer] = 2
        

        if(self.DfsStop):
            return

        checkOfset = lambda i,j,off_i,off_j : self.Puzzle.Board[i+off_i][j+off_j] == 1
        shape = self.Puzzle.Shape
        if currVer == endPoint:
            self.DfsStop =True

            while currVer != None:

                self.Puzzle.Board[currVer] = 3
                currVer = self.DfsDict[currVer] 
        
            return
        if(currVer[0] > 0 and checkOfset(currVer[0],currVer[1],-1,0)):
            
            self.DfsDict[(currVer[0]-1,currVer[1])]=currVer
            self.DfsHelper((currVer[0]-1,currVer[1]),endPoint)
            
        if(currVer[0] < shape[0]-1 and checkOfset(currVer[0],currVer[1],1,0)):
            self.DfsDict[(currVer[0]+1,currVer[1])]=currVer
            self.DfsHelper((currVer[0]+1,currVer[1]),endPoint)

        if(currVer[1] > 0 and checkOfset(currVer[0],currVer[1],0,-1)):
            self.DfsDict[(currVer[0],currVer[1]-1)]=currVer
            self.DfsHelper((currVer[0],currVer[1]-1),endPoint)
            
        if(currVer[1] < shape[1]-1 and checkOfset(currVer[0],currVer[1],0,1)):
            self.DfsDict[(currVer[0],currVer[1]+1)]=currVer
            self.DfsHelper((currVer[0],currVer[1]+1),endPoint)

    def Dfs(self,startPoint:tuple = (-1,-1),endPoint : tuple = (-1,-1)):
        
        if startPoint == (-1,-1):
            startPoint = self.Puzzle.startPoint
        if endPoint == (-1,-1):
            endPoint = self.Puzzle.endPoint

        self.DfsStop = False
        self.DfsDict = dict()
        self.DfsDict[startPoint] = None
        self.Dfs(startPoint,endPoint)

    def Bfs(self,startPoint:tuple = (-1,-1),endPoint : tuple = (-1,-1)):

        if startPoint == (-1,-1):
            startPoint = self.Puzzle.startPoint
        if endPoint == (-1,-1):
            endPoint = self.Puzzle.endPoint

        verQueue = [startPoint]
        self.Puzzle.Board[startPoint] = 2
        shape = self.Puzzle.Shape

        checkOfset = lambda i,j,off_i,off_j : self.Puzzle.Board[i+off_i][j+off_j] == 1
        
        def setCell(currVer:tuple,off_i,off_j):
            i,j= currVer
            verQueue.insert(0,(i+off_i,j+off_j))
            self.Puzzle.Board[(i+off_i,j+off_j)] = 2
            path[(i+off_i,j+off_j)] = (i,j)

        path = dict()
        path[startPoint] = None

        while len(verQueue) > 0:

            currVer = verQueue.pop()

            if(currVer == endPoint):
                
                while currVer != None:
                    self.Puzzle.Board[currVer] = 3
                    currVer = path[currVer]
                return

            if(currVer[0] > 0 and checkOfset(currVer[0],currVer[1],-1,0)):
                setCell(currVer,-1,0)
            
            if(currVer[0] < shape[0]-1 and checkOfset(currVer[0],currVer[1],1,0)):
                setCell(currVer,1,0)
            
            if(currVer[1] > 0 and checkOfset(currVer[0],currVer[1],0,-1)):
                setCell(currVer,0,-1)            
                
            if(currVer[1] < shape[1]-1 and checkOfset(currVer[0],currVer[1],0,1)):
                setCell(currVer,0,1)


    def __init__(self,Puzzle:MazeGen):
        self.DfsStop = False
        self.Puzzle = Puzzle
        self.DfsDict = None

if __name__ == "__main__":

    sys.setrecursionlimit(100000)
    
    m = MazeGen(40)
    s = SearchAlgo(m)
    s.Bfs()
    print(m)
    
    
    