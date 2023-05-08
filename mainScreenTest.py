import turtle as trtl
from turtle import *

from Board import Board

# global configuration and variables

wn = trtl.Screen()

# object intialization

wn.setup(width=850,height=750)

column = 0


boardMaker = trtl.Turtle()
boardMaker.penup()
boardMaker.goto(-350,250)
boardMaker.color("#1F51FF")
boardMaker.shape("square")
boardMaker.pensize(25)
boardMaker.speed(0)

credits = trtl.Turtle()
credits.penup()
credits.goto(-105,-350)
credits.color("blue")
credits.shape("square")

play = trtl.Turtle()
play.penup()
play.goto(105,-350)
play.color("blue")
play.shape("square")

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
    global playBtnPos

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
    boardMaker.goto(250,-220)
    boardMaker.setheading(270)
    boardMaker.pendown()
    boardMaker.fd(35)
    boardMaker.lt(90)
    boardMaker.fd(17)
    boardMaker.lt(180)
    boardMaker.fd(34)
    boardMaker.penup()
    boardMaker.goto(-350,-220)
    boardMaker.setheading(270)
    boardMaker.pendown()
    boardMaker.fd(35)
    boardMaker.lt(90)
    boardMaker.fd(17)
    boardMaker.lt(180)
    boardMaker.fd(34)

    # make the slots of the board
    boardMaker.penup()
    boardMaker.goto(-321,240)
    boardMaker.shape("circle")
    boardMaker.color("white")
    boardMaker.pensize(15)
    boardMaker.setheading(270)
    
    i = -315
    j = 202
    side = []

    playBtnPos= []

    for c in range(7):
        boardMaker.goto(i,j)
        for r in range(6):
            if c==0 and (r==5 or r==3):
                boardMaker.color("yellow")
            elif c==0 and (r==4 or r==2):
                boardMaker.color("red")
            elif c==1 and (r==5 or r==4):
                boardMaker.color("yellow")
            elif c==2 and (r==5 ):
                boardMaker.color("yellow")
            elif c==2 and (r==4 ):
                boardMaker.color("red")
            elif c==3 and (r==5):
                boardMaker.color("red")
            elif c==1 and r==3:
                boardMaker.color("red") 
            else: 
                boardMaker.color("white")
                
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
    
    boardMaker.hideturtle()
    boardMaker.penup()
    boardMaker.color("red")
    boardMaker.goto(-105,275)
    boardMaker.pendown()
    boardMaker.showturtle()
    boardMaker.write("Connect 4",align="center",font=("Verdana",75,"bold"))
    boardMaker.hideturtle()
    credits.goto(-105,-350)
    credits.pendown()
    credits.showturtle()
    credits.write("credits",align="center",font=("Verdana",25,"bold"))
    
    play.goto(105,-270)
    play.pendown()
    play.showturtle()
    play.write("play",align="center",font=("Verdana",25,"bold"))


def clearBoard():
    boardMaker.penup()
    boardMaker.color("blue")
    boardMaker.goto(-350,250)
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
    boardMaker.goto(250,-220)
    boardMaker.setheading(270)
    boardMaker.pendown()
    boardMaker.fd(35)
    boardMaker.lt(90)
    boardMaker.fd(17)
    boardMaker.lt(180)
    boardMaker.fd(34)
    boardMaker.penup()
    boardMaker.goto(-350,-220)
    boardMaker.setheading(270)
    boardMaker.pendown()
    boardMaker.fd(35)
    boardMaker.lt(90)
    boardMaker.fd(17)
    boardMaker.lt(180)
    boardMaker.fd(34)

    # make the slots of the board
    boardMaker.penup()
    boardMaker.goto(-321,240)
    boardMaker.shape("circle")
    boardMaker.color("white")
    boardMaker.pensize(15)
    boardMaker.setheading(270)
    
    i = -315
    j = 202
    side = []

    for c in range(7):
        boardMaker.goto(i,j)
        for r in range(6):
            
            boardMaker.color("white")
                
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
                x = coord[0]
                y =  coord[1]-75
                if y > -98:
                    y += 75
                boardMaker.goto(x,y)
                boardMaker.pendown()
                boardMaker.begin_fill()
                boardMaker.circle(15)
                boardMaker.end_fill()
            elif fakeBoard[c][r] == "o":
                print(f"here is column: {c}")
                print(f"here is row: {r}")
                boardMaker.color("yellow")
                boardMaker.penup()
                coord = boardOutline[c][r]
                print(coord)
                x = coord[0]
                y =  coord[1]-75
                if y > -98:
                    y += 75
                # print(f"here is x: {x}")
                # print(f"here is y: {y}")
                boardMaker.goto(x,y)
                boardMaker.pendown()
                boardMaker.begin_fill()
                boardMaker.circle(15)
                boardMaker.end_fill()

def makeMove(x,y):

    global column
    global currentPlayer
    

    gravity=5
    
    if currentPlayer=="red":
        currentPlayer="yellow"
    else:
        currentPlayer="red"
    play.color(currentPlayer)
    close = []
    closest = 10
    neg = -10
    far = 100
    index = 0
    for i in range(len(boardOutline)):
        for j in boardOutline[i][1]:
            close.append(x-j)
        for num in close:
            if num < closest and num < far and num > neg:
                closest = num
                index = i+1
    print(f"closest: {closest}")
    print(f"column: {index}")
    while fakeBoard[index-1][gravity] in ["x","o"]:
        gravity-=1
        if gravity<0:
            print("You cant make that move")
            return(0)
    if currentPlayer=="red":
        fakeBoard[index][gravity]="x"
    else:
        fakeBoard[index][gravity]="o"

    updateBoard()



def startGame(x,y):
    
    boardMaker.clear()
    
    clearBoard()
    
    boardMaker.penup()
    
    boardMaker.color(currentPlayer)
    
    boardMaker.goto(-150,250)
    # boardMaker.pendown()
    boardMaker.write(f"{currentPlayer}'s Turn",align="center",font=("Verdana",50,"bold"))


    
    
    
    
makeBoard()
# print(playBtnPos)

wn.listen()
# credits.onclick(startGame)
play.onclick(startGame)
# playBtn.onclick(startGame())
wn.onscreenclick(makeMove)

wn.mainloop()