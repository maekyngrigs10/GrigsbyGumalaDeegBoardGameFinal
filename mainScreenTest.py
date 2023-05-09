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
credits.goto(-105,-300)
credits.color("blue")
credits.shape("square")

play = trtl.Turtle()
play.penup()
play.goto(105,-350)
play.color("blue")
play.shape("square")
currentPlayer = "red"
movePiece = trtl.Turtle()
movePiece.penup()
movePiece.goto(-305,250)
movePiece.color(currentPlayer)
movePiece.shape("circle")
movePiece.shapesize(2.5,2.5,1)

direct = trtl.Turtle()
direct.penup()
direct.goto(-250,-350)
direct.color("blue")
direct.shape("square")

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

win = False

# functions


    
def makeMenu():
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
    credits.goto(-105,-300)
    credits.pendown()
    credits.showturtle()
    credits.write("credits",align="center",font=("Verdana",25,"bold"))
    direct.write("Directions",align="center",font=("Verdana",25,"bold"))

    
    play.goto(105,-270)
    play.pendown()
    play.showturtle()
    play.write("play",align="center",font=("Verdana",25,"bold"))


def clearBoard(x,y):

    boardMaker.clear()
    direct.clear()
    credits.clear()
    boardMaker.penup()
    boardMaker.goto(-350,250)
    boardMaker.color("#1F51FF")
    boardMaker.shape("square")
    boardMaker.pensize(25)
    boardMaker.speed(0)


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

def makeCredits(x,y):
    boardMaker.clear()

    credits.penup()
    credits.goto(-0,250)
    credits.write("Credits",align="center",font=("Verdana",100,"bold"))   
    credits.goto(0,150) 
    credits.write("Maekyn Grigsby",align="center",font=("Verdana",50,"bold"))
    credits.goto(0,50) 
    credits.write("Alexander Gumula",align="center",font=("Verdana",50,"bold"))
    credits.goto(0,-50) 
    credits.write("Nicolas Deeg",align="center",font=("Verdana",50,"bold"))

def makeDirects(x,y):
    boardMaker.clear()

    direct.penup()
    direct.goto(-0,250)
    direct.color("black")
    direct.write("Directions",align="center",font=("Verdana",100,"bold"))   
    direct.goto(0,150) 
    direct.color("blue")
    direct.write("Use left and right arrow",align="center",font=("Verdana",40,"bold"))
    direct.goto(0,50) 
    direct.color("red")
    direct.write("Use down arrow to drop piece",align="center",font=("Verdana",40,"bold"))
    direct.goto(0,-50) 
    direct.color("yellow")
    direct.write("And Have Fun!!",align="center",font=("Verdana",40,"bold"))
    direct.hideturtle()

def makeBoard():

    direct.hideturtle()
    boardMaker.penup()
    boardMaker.goto(-350,250)
    boardMaker.color("#1F51FF")
    boardMaker.shape("square")
    boardMaker.pensize(25)
    boardMaker.speed(0)


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
    global currentPlayer
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
                        boardMaker.clear()
                        boardMaker.penup()
                        boardMaker.color(currentPlayer)
                        boardMaker.goto(0,150)
                        boardMaker.write(f"Winner is {currentPlayer}",align="center",font=("Verdana",50,"bold"))
    return(win)

def moveLeft():
    global position
    movePiece.showturtle()
    movePiece.setheading(180)
    if position > 0:
        position-=1
        movePiece.penup()
        movePiece.fd(85)
    else:
        print("invalid beetch")

def moveRight():
    global position
    movePiece.showturtle()
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



wn.listen()

wn.onkeypress(moveLeft,"Left")
wn.onkeypress(moveRight,"Right")
wn.onkeypress(placePiece,"Down")



movePiece.setheading(0)
makeMenu()
wn.listen()

wn.onkeypress(moveLeft,"Left")
wn.onkeypress(moveRight,"Right")
wn.onkeypress(placePiece,"Down")

play.onclick(clearBoard)
credits.onclick(makeCredits)
direct.onclick(makeDirects)
    
# print(playBtnPos)


wn.listen()

wn.mainloop()