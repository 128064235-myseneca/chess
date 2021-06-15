from tkinter import *
import math
from PIL import ImageTk, Image


#####__________ DECLERATIONS __________#####

move = 'White'
isSelect = False
selectedPiece = []#list contains [[piece, piece Image, canvas id], x-index, y-index]
scale = 70
pieceScale = scale - 14
board = []
colorB = "#ddbea9"
colorW = "#fff1e6"
root = Tk()
root.title('PythonGuides')
# ws.geometry('300x300')
# ws.config(bg='#345')
r = ImageTk.PhotoImage(Image.open("chessPieces/blackRook.png").resize(
            (pieceScale, pieceScale)))
n = ImageTk.PhotoImage(Image.open("chessPieces/blackKnight.png").resize(
            (pieceScale, pieceScale)))
b = ImageTk.PhotoImage(Image.open("chessPieces/blackBishop.png").resize(
            (pieceScale, pieceScale)))
kn = ImageTk.PhotoImage(Image.open("chessPieces/blackKing.png").resize(
            (pieceScale, pieceScale)))
q = ImageTk.PhotoImage(Image.open("chessPieces/blackQueen.png").resize(
            (pieceScale, pieceScale)))
p = ImageTk.PhotoImage(Image.open("chessPieces/blackPawn.png").resize(
            (pieceScale, pieceScale)))
R = ImageTk.PhotoImage(Image.open("chessPieces/whiteRook.png").resize(
            (pieceScale, pieceScale)))
N = ImageTk.PhotoImage(Image.open("chessPieces/whiteKnight.png").resize(
            (pieceScale, pieceScale)))
B = ImageTk.PhotoImage(Image.open("chessPieces/whiteBishop.png").resize(
            (pieceScale, pieceScale)))
K = ImageTk.PhotoImage(Image.open("chessPieces/whiteKing.png").resize(
            (pieceScale, pieceScale)))
Q = ImageTk.PhotoImage(Image.open("chessPieces/whiteQueen.png").resize(
            (pieceScale, pieceScale)))
P = ImageTk.PhotoImage(Image.open("chessPieces/whitePawn.png").resize(
            (pieceScale, pieceScale)))
# fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
fen = "4k2r/6r1/8/8/8/8/3R4/R3K3"
testBoard = []# 8x8 board. Each element contains list: [piece, piece Image, canvas id] or ' '




#####__________FUNCTIONS__________#####

def checkSide(piece):
    if piece == ' ':
        return "empty"
    if piece.isupper():
        return "White"
    else:
        return "Black"

def placePiece(testBoard):
    """
    place the pieces on the board
    :param testBoard:
    :return:
    """
    x1 = 0
    y1 = 0
    for i in range(0, 8):
        temp = []
        for j in range(0, 8):
            if(testBoard[i][j] == ' '):
                x1 = x1 + scale
                continue
            testBoard[i][j].append(canvas.create_image(x1+7, y1+7, anchor=NW, image=testBoard[i][j][1]))
            x1 = x1+scale
        board.append(temp)
        x1 = 0
        y1 = y1 + scale

        print(testBoard)
    canvas.update()

def parseFen(test):
    """
    parse the FEN String
    :param test:
    :return:
    """
    for i in range(0,8):
        temp = []
        for j in range(0,len(test[i])):
            print(test[i][j])
            if(test[i][j] == 'r'):
                temp.append(['r',r])
                pass
            elif(test[i][j] == 'n'):
                temp.append(['n',n])
                pass
            elif test[i][j] == 'b':
                temp.append(['b',b])
                pass
            elif test[i][j] == 'q':
                temp.append(['q',q])
                pass
            elif test[i][j] == 'k':
                temp.append(['k',kn])
                pass
            elif test[i][j] == 'b':
                temp.append(['b',b])
                pass
            elif test[i][j] == 'n':
                temp.append(['n',n])
                pass
            elif test[i][j] == 'r':
                temp.append(['r',r])
                pass
            elif test[i][j] == 'p':
                temp.append(['p',p])
                pass
            elif test[i][j] == 'R':
                temp.append(['R',R])
                pass
            elif test[i][j] == 'N':
                temp.append(['N',N])
                pass
            elif test[i][j] == 'B':
                temp.append(['B',B])
                pass
            elif test[i][j] == 'K':
                temp.append(['K',K])
                pass
            elif (test[i][j] == 'Q'):
                temp.append(['Q',Q])
                pass
            elif (test[i][j] == 'B'):
                temp.append(['B',B])
                pass
            elif (test[i][j] == 'N'):
                temp.append(['N',N])
                pass
            elif test[i][j] == 'R':
                temp.append(['R',R])
                pass
            elif test[i][j] == 'P':
                temp.append(['P',P])
                pass
            elif test[i][j] == '1':
                for k in range(0,1):
                    temp.append(' ')
                pass
            elif test[i][j] == '2':
                for k in range(0, 2):
                    temp.append(' ')
                pass
            elif test[i][j] == '3':
                for k in range(0, 3):
                    temp.append(' ')
                pass
            elif test[i][j] == '4':
                for k in range(0, 4):
                    temp.append(' ')
                pass
            elif test[i][j] == '5':
                for k in range(0, 5):
                    temp.append(' ')
                pass
            elif test[i][j] == '6':
                for k in range(0, 6):
                    temp.append(' ')
                pass
            elif (test[i][j] == '7'):
                for k in range(0,7):
                    temp.append(' ')
                pass
            elif (test[i][j] == '8'):
                for k in range(0,8):
                    temp.append(' ')
                pass

        testBoard.append(temp)

def buttonClick():
    print("click")
    global colorB
    colorB="blue"
    for i in range(0, 8):
        for j in range(0, 8):

            canvas.itemconfig(board[i][j], fill=colorB if ((i + j) % 2 == 0) else colorW)


    # root.update()

def clickOnBoard(event):
    print(event.x, event.y)
    x = math.floor(event.x/scale)
    y = math.floor(event.y/scale)
    global isSelect
    global selectedPiece
    global testBoard
    global move
    if isSelect == False:
        """
            If piece is not selected
        """
        if(testBoard[y][x] == ' '):
            isSelect = False
            print("not select")
        else:
            if checkSide(testBoard[y][x][0]) == move:
                isSelect = True
                selectedPiece = [testBoard[y][x],x,y]
                print("select")
            else:
                print("not select")
        print(str(x) + "," + str(y))
    else:
        """
            If piece is selected
            Here, the move is placed
        """
        print(selectedPiece)
        if (checkTake(x,y) == True):
            canvas.delete(testBoard[y][x][2])
            print("delete")
        elif (checkTake(x,y) == False):
            print("not move")
            isSelect = False
            return


        if (x == selectedPiece[1] and (y == selectedPiece[2])):
            #Check if the move is the same place

            isSelect = False
            print("same place")
            return()

        testBoard[selectedPiece[2]][selectedPiece[1]] = ' '
        testBoard[y][x] = selectedPiece[0]
        canvas.move(selectedPiece[0][2], (x-selectedPiece[1])*scale, (y-selectedPiece[2])*scale)

        if move == "White":
            move = "Black"
        else:
            move = "White"

        isSelect = False
        print("moved")
    return()

def generateBoard():
    x1 = 0
    y1 = 0
    x2 = scale
    y2 = scale

    for i in range(0, 8):
        temp = []
        for j in range(0, 8):
            temp.append(canvas.create_rectangle(
                x1, y1, x2, y2,
                fill=colorB if ((i + j) % 2 == 0) else colorW))
            x1 = x1 + scale
            x2 = x2 + scale
        board.append(temp)
        print(temp)
        x1 = 0
        y1 = y1 + scale
        y2 = y2 + scale

def checkTake(x,y):
    global testBoard
    global selectedPiece
    global move
    print(1, testBoard[y][x][0])

    if (checkSide(testBoard[y][x][0]) == "Black" and move == "Black") or (checkSide(testBoard[y][x][0]) == "White" and move == "White"):
        print("Cant be moved")
        return False
    elif (checkSide(testBoard[y][x][0]) == "Black" and move == "White") or (checkSide(testBoard[y][x][0]) == "White" and move == "Black"):
        print("Can take")
        return True
    else:
        return "empty"



def isValidMove():
    pass


#####__________MAIN__________#####


parseFenString = fen.split("/")
parseFen(parseFenString)
canvas = Canvas(
    root,
    height=scale*8,
    width=scale*8,
    bg="#fff"
)
canvas.grid(row=0, column=0, rowspan=4)
canvas.bind("<Button-1>", clickOnBoard)


generateBoard()

placePiece(testBoard)


button_color = Button(root, text="click", command=buttonClick)
button_color.grid(row=0, column=1)

root.mainloop()