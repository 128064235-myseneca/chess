from tkinter import *
import math
from PIL import ImageTk, Image

#####__________ DECLARATIONS __________#####

move = 'White'
check = False
isSelect = False
selectedPiece = []  # list contains [[piece, piece Image, canvas id], x-index, y-index]
scale = 70
pieceScale = scale - 14
board = []
colorB = "#ddbea9"
colorW = "#fff1e6"
root = Tk()
root.title('PythonGuides')
validSquares = []
blackPawnInitialFlag = [1, 1, 1, 1, 1, 1, 1, 1]
whitePawnInitialFlag = [1, 1, 1, 1, 1, 1, 1, 1]
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
fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
# fen = "8/PPPPPPPP/8/8/8/8/pppppppp/8"
# fen = "rnbqkbnr/8/8/8/8/8/8/RNBQKBNR"
# fen = "3Bk2r/5brn/8/8/8/8/3R4/R3K3"
testBoard = []  # 8x8 board. Each element contains list: [piece, piece Image, canvas id] or ' '


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
            if (testBoard[i][j] == ' '):
                x1 = x1 + scale
                continue
            testBoard[i][j].append(canvas.create_image(x1 + 7, y1 + 7, anchor=NW, image=testBoard[i][j][1]))
            if testBoard[i][j][0] == 'p' or testBoard[i][j][0] == 'P':
                testBoard[i][j].append('1')
            x1 = x1 + scale
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
    for i in range(0, 8):
        temp = []
        for j in range(0, len(test[i])):
            print(test[i][j])
            if test[i][j] == 'r':
                temp.append(['r', r])
                pass
            elif test[i][j] == 'n':
                temp.append(['n', n])
                pass
            elif test[i][j] == 'b':
                temp.append(['b', b])
                pass
            elif test[i][j] == 'q':
                temp.append(['q', q])
                pass
            elif test[i][j] == 'k':
                temp.append(['k', kn])
                pass
            elif test[i][j] == 'b':
                temp.append(['b', b])
                pass
            elif test[i][j] == 'n':
                temp.append(['n', n])
                pass
            elif test[i][j] == 'r':
                temp.append(['r', r])
                pass
            elif test[i][j] == 'p':
                temp.append(['p', p])
                pass
            elif test[i][j] == 'R':
                temp.append(['R', R])
                pass
            elif test[i][j] == 'N':
                temp.append(['N', N])
                pass
            elif test[i][j] == 'B':
                temp.append(['B', B])
                pass
            elif test[i][j] == 'K':
                temp.append(['K', K])
                pass
            elif test[i][j] == 'Q':
                temp.append(['Q', Q])
                pass
            elif test[i][j] == 'B':
                temp.append(['B', B])
                pass
            elif test[i][j] == 'N':
                temp.append(['N', N])
                pass
            elif test[i][j] == 'R':
                temp.append(['R', R])
                pass
            elif test[i][j] == 'P':
                temp.append(['P', P])
                pass
            elif test[i][j] == '1':
                for k in range(0, 1):
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
            elif test[i][j] == '7':
                for k in range(0, 7):
                    temp.append(' ')
                pass
            elif test[i][j] == '8':
                for k in range(0, 8):
                    temp.append(' ')
                pass

        testBoard.append(temp)


def buttonClick():
    print("click")
    global colorB
    colorB = "blue"
    for i in range(0, 8):
        for j in range(0, 8):
            canvas.itemconfig(board[i][j], fill=colorB if ((i + j) % 2 == 0) else colorW)

    # root.update()

def isCheck():
    pass

def clickOnBoard(event):
    print(event.x, event.y)
    x = math.floor(event.x / scale)
    y = math.floor(event.y / scale)
    global isSelect
    global selectedPiece
    global testBoard
    global move
    if isSelect == False:
        """
            If piece is not selected
        """
        if (testBoard[y][x] == ' '):
            isSelect = False
        else:
            if checkSide(testBoard[y][x][0]) == move and check == False:
                selectedPiece = [testBoard[y][x], x, y]
                isValidMove()
                isSelect = True
            else:
                pass
        print(str(x) + "," + str(y))
    else:
        """
            If piece is selected
            Here, the move is placed
        """
        print(selectedPiece)

        if ([x, y] in validSquares):
            if (checkTake(x, y) == True):
                """
                    take a piece
                """
                canvas.delete(testBoard[y][x][2])

            elif (checkTake(x, y) == False):
                isSelect = False
                return

            if (x == selectedPiece[1] and (y == selectedPiece[2])):
                # Check if the move is the same place
                isSelect = False
                return ()

            testBoard[selectedPiece[2]][selectedPiece[1]] = ' '

            #Logic for initial 2 step movement of pawn
            if (selectedPiece[0][0] == 'p' or selectedPiece[0][0] == 'P') and selectedPiece[0][3] == '1':
                selectedPiece[0][3] = '0'

            testBoard[y][x] = selectedPiece[0]
            canvas.move(selectedPiece[0][2], (x - selectedPiece[1]) * scale, (y - selectedPiece[2]) * scale)
            if selectedPiece[0][0] == 'p' or selectedPiece[0][0] == 'P':
                selectedPiece[0][3] = 0

            # Promote the pawn to Queen
            if (selectedPiece[0][0] == 'p' or selectedPiece[0][0] == 'P') and (y == 7 or y == 0):
                canvas.delete(testBoard[y][x][2])
                testBoard[y][x] = ['q' if move == 'Black' else 'Q', q if move == 'Black' else Q, canvas.create_image(x*scale + 7, y*scale + 7, anchor=NW, image=q if move == 'Black' else Q)]
                print(testBoard[y][x])
                print("Promoted")
            # Change the turns
            if move == "White":
                move = "Black"
            else:
                move = "White"

            isSelect = False
            print("moved")
            print("true square")
        else:
            isSelect = False
            print("not true square")
        resetPossibleMoveColor()

    return ()


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


def checkTake(x, y):
    global testBoard
    global selectedPiece
    global move
    print(1, testBoard[y][x][0])

    if (checkSide(testBoard[y][x][0]) == "Black" and move == "Black") or (
            checkSide(testBoard[y][x][0]) == "White" and move == "White"):
        print("Cant be moved")
        return False
    elif (checkSide(testBoard[y][x][0]) == "Black" and move == "White") or (
            checkSide(testBoard[y][x][0]) == "White" and move == "Black"):
        print("Can take")
        return True
    else:
        return "empty"


def checkDiagonalMove(x, y):
    # Down-Right  Movement
    for i, j in zip(range(x + 1, 8), range(y + 1, 8)):
        # check for barrier
        if testBoard[j][i] == ' ':
            validSquares.append([i, j])
        else:
            if (move == "Black" and checkSide(testBoard[j][i][0]) == "White") or (
                    move == "White" and checkSide(testBoard[j][i][0]) == "Black"):
                validSquares.append([i, j])  # takes square
            break

    # Up-Left Movement
    for i, j in zip(range(x - 1, -1, -1), range(y - 1, -1, -1)):
        # check for barrier
        if testBoard[j][i] == ' ':
            validSquares.append([i, j])
        else:
            if (move == "Black" and checkSide(testBoard[j][i][0]) == "White") or (
                    move == "White" and checkSide(testBoard[j][i][0]) == "Black"):
                validSquares.append([i, j])  # takes square
            break

    # Down-Left Movement
    for i, j in zip(range(x - 1, -1, -1), range(y + 1, 8)):
        # check for barrier
        if (testBoard[j][i] == ' '):
            validSquares.append([i, j])
        else:
            if (move == "Black" and checkSide(testBoard[j][i][0]) == "White") or (
                    move == "White" and checkSide(testBoard[j][i][0]) == "Black"):
                validSquares.append([i, j])  # takes square
            break
    # Up-Right Movement
    for i, j in zip(range(x + 1, 8), range(y - 1, -1, -1)):
        # check for barrier

        if (testBoard[j][i] == ' '):
            validSquares.append([i, j])
        else:
            if (move == "Black" and checkSide(testBoard[j][i][0]) == "White") or (
                    move == "White" and checkSide(testBoard[j][i][0]) == "Black"):
                validSquares.append([i, j])  # takes square
            break

    pass


def checkLineMove(x, y):
    for i in range(x + 1, 8):
        # check for barrier
        if (testBoard[y][i] == ' '):
            validSquares.append([i, y])
        else:
            if (move == "Black" and checkSide(testBoard[y][i][0]) == "White") or (
                    move == "White" and checkSide(testBoard[y][i][0]) == "Black"):
                validSquares.append([i, y])  # takes square
            break

        # Left Movement
    for i in range(x - 1, -1, -1):
        # check for barrier
        if (testBoard[y][i] == ' '):
            validSquares.append([i, y])
        else:
            if (move == "Black" and checkSide(testBoard[y][i][0]) == "White") or (
                    move == "White" and checkSide(testBoard[y][i][0]) == "Black"):
                validSquares.append([i, y])  # takes square
            break

        # Up Movement
    for i in range(y - 1, -1, -1):
        # check for barrier
        if (testBoard[i][x] == ' '):
            validSquares.append([x, i])
        else:
            if (move == "Black" and checkSide(testBoard[i][x][0]) == "White") or (
                    move == "White" and checkSide(testBoard[i][x][0]) == "Black"):
                validSquares.append([x, i])  # takes square
            break

        # Down Movement
    for i in range(y + 1, 8):
        # check for barrier
        if (testBoard[i][x] == ' '):
            validSquares.append([x, i])
        else:
            if (move == "Black" and checkSide(testBoard[i][x][0]) == "White") or (
                    move == "White" and checkSide(testBoard[i][x][0]) == "Black"):
                validSquares.append([x, i])  # takes square
            break


def isValidMove():
    x = selectedPiece[1]
    y = selectedPiece[2]

    ####________PAWN MOVEMENT________####

    if selectedPiece[0][0] == 'p' or selectedPiece[0][0] == 'P':
        moveOffsetBlack = [[0, 1]]
        moveOffsetWhite = [[0, -1]]
        InitialMoveOffsetBlack = [[0, 2]]
        InitialMoveOffsetWhite = [[0, -2]]
        moveOffsetBlackTake = [[1, 1], [-1, 1]]
        moveOffsetWhiteTake = [[-1, -1], [1, -1]]

        temp_x = x + (moveOffsetBlack[0][0] if selectedPiece[0][0] == "p" else moveOffsetWhite[0][0])
        temp_y = y + (moveOffsetBlack[0][1] if selectedPiece[0][0] == "p" else moveOffsetWhite[0][1])
        if (8 > temp_x >= 0) and (8 > temp_y >= 0) and (testBoard[temp_y][temp_x] == ' '):
            validSquares.append([temp_x, temp_y])

        temp_x = x + (InitialMoveOffsetBlack[0][0] if selectedPiece[0][0] == "p" else InitialMoveOffsetWhite[0][0])
        temp_y = y + (InitialMoveOffsetBlack[0][1] if selectedPiece[0][0] == "p" else InitialMoveOffsetWhite[0][1])
        if (8 > temp_x >= 0) and (8 > temp_y >= 0) and (testBoard[temp_y][temp_x] == ' ' and selectedPiece[0][3] == '1'):
            # Logic for initial 2 step movement of pawn
            validSquares.append([temp_x, temp_y])


        for i in range(0, len(moveOffsetBlackTake)):
            temp_x = x + (moveOffsetBlackTake[i][0] if selectedPiece[0][0] == "p" else moveOffsetWhiteTake[i][0])
            temp_y = y + (moveOffsetBlackTake[i][1] if selectedPiece[0][0] == "p" else moveOffsetWhiteTake[i][1])

            if (8 > temp_x >= 0) and (8 > temp_y >= 0) and (
                    (checkSide(testBoard[temp_y][temp_x][0]) == 'Black' and move == "White") or (
                    checkSide(testBoard[temp_y][temp_x][0]) == 'White' and move == "Black")):
                validSquares.append([temp_x, temp_y])  # takes square

    ####________QUEEN MOVEMENT________####
    if selectedPiece[0][0] == 'q' or selectedPiece[0][0] == 'Q':
        checkDiagonalMove(x, y)
        checkLineMove(x, y)
    ####________KING MOVEMENT________####
    if selectedPiece[0][0] == 'k' or selectedPiece[0][0] == 'K':
        offset = [[1, 0],
                  [1, 1],
                  [-1, 0],
                  [-1, -1],
                  [0, -1],
                  [-1, 1],
                  [1, -1],
                  [0, 1]]

        for i in range(0, len(offset)):
            temp_x = x + offset[i][0]
            temp_y = y + offset[i][1]

            if (8 > temp_x >= 0) and (8 > temp_y >= 0) and (testBoard[temp_y][temp_x] == ' '):
                validSquares.append([temp_x, temp_y])
            if (8 > temp_x >= 0) and (8 > temp_y >= 0) and (
                    (checkSide(testBoard[temp_y][temp_x][0]) == 'Black' and move == "White") or (
                    checkSide(testBoard[temp_y][temp_x][0]) == 'White' and move == "Black")):
                validSquares.append([temp_x, temp_y])  # takes square

    ####________BISHOP MOVEMENT________####
    if selectedPiece[0][0] == 'b' or selectedPiece[0][0] == 'B':
        checkDiagonalMove(x, y)

    ####________KNIGHT MOVEMENT________####
    if selectedPiece[0][0] == 'n' or selectedPiece[0][0] == 'N':
        offset = [[-2, 1],
                  [-1, 2],
                  [1, 2],
                  [2, 1],
                  [2, -1],
                  [1, -2],
                  [-1, -2],
                  [-2, -1]]

        for i in range(0, len(offset)):
            temp_x = x + offset[i][0]
            temp_y = y + offset[i][1]

            if (8 > temp_x >= 0) and (8 > temp_y >= 0) and (testBoard[temp_y][temp_x] == ' '):
                validSquares.append([temp_x, temp_y])
            if (8 > temp_x >= 0) and (8 > temp_y >= 0) and (
                    (checkSide(testBoard[temp_y][temp_x][0]) == 'Black' and move == "White") or (
                    checkSide(testBoard[temp_y][temp_x][0]) == 'White' and move == "Black")):
                validSquares.append([temp_x, temp_y])  # takes square

    ####________ROOK MOVEMENT________####

    if selectedPiece[0][0] == 'r' or selectedPiece[0][0] == 'R':
        checkLineMove(x, y)

    print(validSquares)
    possibleMoveColor(validSquares)


def possibleMoveColor(possibleMoves):
    for i in range(0, len(possibleMoves)):
        canvas.itemconfig(board[possibleMoves[i][1]][possibleMoves[i][0]], fill="#cb997e")


def resetPossibleMoveColor():
    global validSquares
    print("reset")
    for i in range(0, len(validSquares)):
        canvas.itemconfig(board[validSquares[i][1]][validSquares[i][0]],
                          fill=colorB if ((validSquares[i][1] + validSquares[i][0]) % 2 == 0) else colorW)
    validSquares = []


#####__________MAIN__________#####


parseFenString = fen.split("/")
parseFen(parseFenString)
canvas = Canvas(
    root,
    height=scale * 8,
    width=scale * 8,
    bg="#fff"
)
canvas.grid(row=0, column=0, rowspan=4)
canvas.bind("<Button-1>", clickOnBoard)

generateBoard()

placePiece(testBoard)

button_color = Button(root, text="click", command=buttonClick)
button_color.grid(row=0, column=1)

root.mainloop()
