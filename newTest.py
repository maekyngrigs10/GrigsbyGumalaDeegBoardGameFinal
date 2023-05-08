# imports

import turtle as trtl
from turtle import *
from Board import Board

# global configuration and variables

wn = trtl.Screen()

# object intialization

wn.setup(width=850,height=750)
currentPlayer = "red"
gravity = 5

boardMaker = trtl.Turtle()
boardMaker.penup()
boardMaker.goto(-400,250)
boardMaker.color("#1F51FF")
boardMaker.shape("square")
boardMaker.pensize(25)
boardMaker.speed(0)

movePiece = trtl.Turtle()
movePiece.penup()
movePiece.goto(-355,300)
movePiece.color(currentPlayer)
movePiece.shape("circle")
movePiece.shapesize(2.5,2.5,1)

position = 0

# variables

board = []
boardOutline = []
fakeBoard=[["-","-","-","-","-","-"],
           ["-","-","-","-","-","-"],
           ["-","-","-","-","-","-"],
           ["-","-","-","-","-","-"],
           ["-","-","-","-","-","-"],
           ["-","-","-","-","-","-"],
           ["-","-","-","-","-","-"]]
currentPlayer = "red"
win = False

# functions

def makeBoard():

    # make the outline of the board
    boardMaker.begin_fill()
    boardMaker.pendown()
    boardMaker.setheading(0)
    for i in range(2):
        boardMaker.fd(600)
        boardMaker.rt(90)
        boardMaker.fd(480)
        boardMaker.rt(90)
    boardMaker.end_fill()
    boardMaker.penup()
    boardMaker.goto(200,-220)
    boardMaker.setheading(270)
    boardMaker.pendown()
    boardMaker.fd(35)
    boardMaker.lt(90)
    boardMaker.fd(17)
    boardMaker.lt(180)
    boardMaker.fd(34)
    boardMaker.penup()
    boardMaker.goto(-400,-220)
    boardMaker.setheading(270)
    boardMaker.pendown()
    boardMaker.fd(35)
    boardMaker.lt(90)
    boardMaker.fd(17)
    boardMaker.lt(180)
    boardMaker.fd(34)

    # make the slots of the board
    boardMaker.penup()
    boardMaker.goto(-371,240)
    boardMaker.shape("circle")
    boardMaker.color("white")
    boardMaker.pensize(15)
    boardMaker.setheading(270)
    
    i = -371
    j = 202
    side = []

    for c in range(7):
        boardMaker.goto(i,j)
        for r in range(6):
            boardMaker.pendown()
            boardMaker.begin_fill()
            boardMaker.circle(15)
            boardMaker.end_fill()
            boardMaker.penup()
            boardMaker.fd(75)
            j -= 50
            side.append([i,j])
            board.append([c,r+1])
        i += 85
        j = 202
        boardOutline.append(side)
        side = []
    
    boardMaker.penup()
    boardMaker.goto(250,250)
    boardMaker.color("#1F51FF")
    boardMaker.pendown()
    boardMaker.setheading(0)
    
    boardMaker.begin_fill()
    for i in range(2):
        boardMaker.fd(100)
        boardMaker.rt(90)
        boardMaker.fd(500)
        boardMaker.rt(90)
    boardMaker.end_fill()

def updateBoard():
    global fakeBoard
    global board
    global boardOutline

    for c in range(len(fakeBoard)):
        for r in range(len(fakeBoard[c])):
            if fakeBoard[c][r] == "x":
                boardMaker.color("red")
                boardMaker.penup()
                coord = boardOutline[c][r]
                x = coord[0]+15
                y = coord[1]-75
                if r == 1:
                    y= -192
                elif r==2:
                    y = -162
                else:
                    y+=11
                
                print(f"x: {x} \t y: {y}")
                boardMaker.goto(x,y)
                boardMaker.pendown()
                boardMaker.begin_fill()
                boardMaker.circle(15)
                boardMaker.end_fill()
            elif fakeBoard[c][r] == "o":
                boardMaker.color("yellow")
                boardMaker.penup()
                coord = boardOutline[c][r]
                x = coord[0]+15
                y =  coord[1]-75

                if r==0:
                    y= -192
                elif r==2:
                    y = -112
                else:
                    y+=11

                print(f"x: {x} \t y: {y}")
                # if y > -98:
                #     y += 75
                # print(f"here is x: {x}")
                # print(f"here is y: {y}")
                boardMaker.goto(x,y)
                boardMaker.pendown()
                boardMaker.begin_fill()
                boardMaker.circle(15)
                boardMaker.end_fill()
def checkForWins():
    global win
    for word in ["xxxx","oooo"]: #pulls word to search for
        for row in range(len(fakeBoard)): #imagin a pointer combing through every row and column of the word search.
            for column in range(len(fakeBoard[row])):
                for scanDirection in [[1,0,"down"],[-1,0,"up"],[0,1,"right"],[0,-1,"left"],[1,1,"right down"],[-1,-1,"left up"],[1,-1,"left down"],[-1,1,"right up"]]: #the scan direction is the direction that the word is going
                    checksum=0 #the checksum should equal the word length. if it does then the word was found.
                    for i in range(len(word)):
                        if (row+(i*scanDirection[0]))<0 or (row+(i*scanDirection[0]))>(len(fakeBoard)-1) or (column+(i*scanDirection[1]))<0 or (column+(i*scanDirection[1]))>(len(fakeBoard[row])-1): #makes sure the scanner doesn't go out of bounds
                            pass
                        elif word[i].lower()==fakeBoard[row+(i*scanDirection[0])][column+(i*scanDirection[1])].lower():#each letter is thouroughly checked
                            checksum+=1
                    if checksum==len(word):
                        win=True #makes a list of where the words are
                        print("winner")
    return(win)

def moveLeft():
    global position
    movePiece.setheading(180)
    if position > 0:
        position-=1
        movePiece.penup()
        movePiece.fd(85)
    else:
        print("invalid beetch")

def moveRight():
    global position
    movePiece.setheading(0)
    if position <= 5:
        position+=1
        movePiece.penup()
        movePiece.fd(85)

    else:
        print("invalid beetch")

def placePiece():
    global position
    global gravity
    global currentPlayer
    gravity=5
    
    if currentPlayer=="red":
        currentPlayer="yellow"
    else:
        currentPlayer="red"
    
    while fakeBoard[position][gravity] in ["x","o"]:
        gravity-=1
        if gravity<0:
            print("You cant make that move")
            return(0)
    
    if currentPlayer=="red":
        fakeBoard[position][gravity]="x"
    else:
        fakeBoard[position][gravity]="o"

    print(fakeBoard)
    updateBoard()
    checkForWins()


movePiece.setheading(0)
makeBoard()
wn.listen()

wn.onkeypress(moveLeft,"Left")
wn.onkeypress(moveRight,"Right")
wn.onkeypress(placePiece,"Down")



wn.mainloop()
