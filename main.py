from tkinter.ttk import Style
from MazeGenerator import Maze
from tkinter import *


def main():

    boxWidth = 7

    m = Maze(100)
    root = Tk()
    print(m)

    root.configure(background='black')
    canvas = Canvas(root, width=m.Shape[0]*boxWidth, height=m.Shape[1]*boxWidth,background='black',border=0)
    canvas.pack()
    for i in range(m.Shape[0]):
        for j in range(m.Shape[1]):
            if( m.Board[i][j] == 1):
                canvas.create_rectangle(j*boxWidth, i*boxWidth, j*boxWidth+boxWidth, i*boxWidth+boxWidth, fill='white')

 
    root.mainloop()

if __name__ == "__main__":
    main()