#! python3

import re, sys, os
from copy import copy

class HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout

def printBoard(board):
    print(r'------------------------------------------------------------------------------')
    print(r'| ||\\\\\\|        |\\\\\\|        |\\\\\\|        |\\\\\\|        | |       |')
    print(r'| ||\\' + board['a8'] + r'\\|   ' + board['b8'] + r'   |\\' + board['c8'] + r'\\|   ' + board['d8'] + r'   |\\' + board['e8'] + r'\\|   ' + board['f8'] + r'   |\\' + board['g8'] + r'\\|   ' + board['h8'] + r'   | |   8   |')
    print(r'| ||\\\\\\|        |\\\\\\|        |\\\\\\|        |\\\\\\|        | |       |')
    print(r'| |----------------------------------------------------------------| |       |')
    print(r'| |        |\\\\\\|        |\\\\\\|        |\\\\\\|        |\\\\\\|| |       |')
    print(r'| |   ' + board['a7'] + r'   |\\' + board['b7'] + r'\\|   ' + board['c7'] + r'   |\\' + board['d7'] + r'\\|   ' + board['e7'] + r'   |\\' + board['f7'] + r'\\|   ' + board['g7'] + r'   |\\' + board['h7'] + r'\\|| |   7   |')
    print(r'| |        |\\\\\\|        |\\\\\\|        |\\\\\\|        |\\\\\\|| |       |')
    print(r'| |----------------------------------------------------------------| |       |')
    print(r'| ||\\\\\\|        |\\\\\\|        |\\\\\\|        |\\\\\\|        | |       |')
    print(r'| ||\\' + board['a6'] + r'\\|   ' + board['b6'] + r'   |\\' + board['c6'] + r'\\|   ' + board['d6'] + r'   |\\' + board['e6'] + r'\\|   ' + board['f6'] + r'   |\\' + board['g6'] + r'\\|   ' + board['h6'] + r'   | |   6   |')
    print(r'| ||\\\\\\|        |\\\\\\|        |\\\\\\|        |\\\\\\|        | |       |')
    print(r'| |----------------------------------------------------------------| |       |')
    print(r'| |        |\\\\\\|        |\\\\\\|        |\\\\\\|        |\\\\\\|| |       |')
    print(r'| |   ' + board['a5'] + r'   |\\' + board['b5'] + r'\\|   ' + board['c5'] + r'   |\\' + board['d5'] + r'\\|   ' + board['e5'] + r'   |\\' + board['f5'] + r'\\|   ' + board['g5'] + r'   |\\' + board['h5'] + r'\\|| |   5   |')
    print(r'| |        |\\\\\\|        |\\\\\\|        |\\\\\\|        |\\\\\\|| |       |')
    print(r'| |----------------------------------------------------------------| |       |')
    print(r'| ||\\\\\\|        |\\\\\\|        |\\\\\\|        |\\\\\\|        | |       |')
    print(r'| ||\\' + board['a4'] + r'\\|   ' + board['b4'] + r'   |\\' + board['c4'] + r'\\|   ' + board['d4'] + r'   |\\' + board['e4'] + r'\\|   ' + board['f4'] + r'   |\\' + board['g4'] + r'\\|   ' + board['h4'] + r'   | |   4   |')
    print(r'| ||\\\\\\|        |\\\\\\|        |\\\\\\|        |\\\\\\|        | |       |')
    print(r'| |----------------------------------------------------------------| |       |')
    print(r'| |        |\\\\\\|        |\\\\\\|        |\\\\\\|        |\\\\\\|| |       |')
    print(r'| |   ' + board['a3'] + r'   |\\' + board['b3'] + r'\\|   ' + board['c3'] + r'   |\\' + board['d3'] + r'\\|   ' + board['e3'] + r'   |\\' + board['f3'] + r'\\|   ' + board['g3'] + r'   |\\' + board['h3'] + r'\\|| |   3   |')
    print(r'| |        |\\\\\\|        |\\\\\\|        |\\\\\\|        |\\\\\\|| |       |')
    print(r'| |----------------------------------------------------------------| |       |')
    print(r'| ||\\\\\\|        |\\\\\\|        |\\\\\\|        |\\\\\\|        | |       |')
    print(r'| ||\\' + board['a2'] + r'\\|   ' + board['b2'] + r'   |\\' + board['c2'] + r'\\|   ' + board['d2'] + r'   |\\' + board['e2'] + r'\\|   ' + board['f2'] + r'   |\\' + board['g2'] + r'\\|   ' + board['h2'] + r'   | |   2   |')
    print(r'| ||\\\\\\|        |\\\\\\|        |\\\\\\|        |\\\\\\|        | |       |')
    print(r'| |----------------------------------------------------------------| |       |')
    print(r'| |        |\\\\\\|        |\\\\\\|        |\\\\\\|        |\\\\\\|| |       |')
    print(r'| |   ' + board['a1'] + r'   |\\' + board['b1'] + r'\\|   ' + board['c1'] + r'   |\\' + board['d1'] + r'\\|   ' + board['e1'] + r'   |\\' + board['f1'] + r'\\|   ' + board['g1'] + r'   |\\' + board['h1'] + r'\\|| |   1   |')
    print(r'| |        |\\\\\\|        |\\\\\\|        |\\\\\\|        |\\\\\\|| |       |')
    print(r'| |----------------------------------------------------------------| |-------|')
    print(r'| |    a      b       c       d       e       f        g       h   | |///////|')
    print(r'------------------------------------------------------------------------------')

def game():
    t = 'W'
    tN = 1
    print("It is White's turn.")
    while True:
        p = ''
        m = ''
        
        p = pickPiece(t)
        if p == 'restart':
            return True
    
        works, m = pickMove(t, p)
        
        if works == 'y':
            r, t, tN = changeTurn(p, m, t, tN)
            if r == True:
                return True

def pickPiece(turn):
    while True:
            print("Which piece would you like to move: ", end="")
            piece = input()
            if piece == 'exit':
                exit()
            elif piece == 'restart':
                return piece
            elif piece in spaces:
                attempt[piece] = spaces[piece]
                if turn == spaces[piece][0]:
                    return piece
                else:
                    print("Pick your own piece.")

def pickMove(turn, piece):
    while piece != 'restart':
        print("Where would you like to move it: ", end="")
        move = input()
        if move in spaces:
            attempt[move] = attempt[piece]
            attempt[piece] = '  '
            if turn == spaces[move][0]:
                print("You can't move ontop of your own piece.")
                return 'n', move
            elif check(attempt, isKing(turn)) == False:
                if chessPiece(spaces, piece, move) == True:
                    return 'y', move
                else:
                    return 'n', move
            elif check(attempt, isKing(turn)) == True:
                print("That move would put you in check.")
                return 'n', move
            else:
                return 'n', move
        

def changeTurn(piece, move, turn, turnNum):
    spaces[move] = attempt[move]
    spaces[piece] = attempt[piece]
    printBoard(spaces)
    if spaces[move][1] == 'P':
        pawnSwap(move)
            
    if turn == 'W':
        moveList.setdefault(turnNum, [[piece, move]])
        turn = 'B'
    else:
        moveList[turnNum].append([piece, move])
        turnNum += 1
        turn = 'W'

    if check(spaces, isKing(turn)) == True:
        if checkMate(turn, isKing(turn)) == True:
            print("Checkmate.")
            return True, turn, turnNum
        else:
            print("Check.")

    if turn == 'W':
        print("It is White's turn.")
    else:
        print("It is Black's turn.")
    print(moveList)
    return False, turn, turnNum

def restart():
    print("Would you like to restart the game? (y/n)")
    answer = input()
    while True:
        if answer == 'y':
            return 'y'
        elif answer == 'n':
            print("Would you like to exit? (y/n)")
            done = input()
            if done == 'y':
                return 'n'

def left(place):
    return (chr(ord(place[0]) - 1) + place[1])
def upLeft(place):
    return (chr(ord(place[0]) - 1) + str(int(place[1]) + 1))
def up(place):
    return place[0] + str((int(place[1]) + 1))
def upRight(place):
    return (chr(ord(place[0]) + 1) + str(int(place[1]) + 1))
def right(place):
    return (chr(ord(place[0]) + 1) + place[1])
def downLeft(place):
    return (chr(ord(place[0]) - 1) + str(int(place[1]) - 1))
def down(place):
    return place[0] + str((int(place[1]) - 1))
def downRight(place):
    return (chr(ord(place[0]) + 1) + str(int(place[1]) - 1))

def chessPiece(n, a, b):
    if spaces[a][1] == 'P':
        return pawn(n, a, b)
    elif spaces[a][1] == 'R':
        return rook(n, a, b)
    elif spaces[a][1] == 'N':
        return knight(a, b)
    elif spaces[a][1] == 'B':
        return bishop(n, a, b)
    elif spaces[a][1] == 'Q':
        return queen(n, a, b)
    elif spaces[a][1] == 'K':
        return king(a, b)
    else:
        print("No piece chosen...")
        return False

def pawn(version, start, end): 
    if version[start][0] == 'W': # White Pawns
        if upLeft(start) == end and version[upLeft(start)] != '  ':
            return True
        elif upRight(start) == end and version[upRight(start)] != '  ':
            return True
        elif version[up(start)] != '  ':
            print("Invalid move.")
            return False
        elif start[1] == '2':
            if up(start) == end:
                return True
            elif up(up(start)) == end and version[end] == '  ':
                return True
            else:
                print("Invalid move.")
                return False
        elif up(start) == end:
            return True
        else:
            print("Invalid move.")
            return False

    elif version[start][0] == 'B': # Black Pawns
        if downLeft(start) == end and version[downLeft(start)] != '  ':
            return True
        elif downRight(start) == end and version[downRight(start)] != '  ':
            return True
        elif version[down(start)] != '  ':
            return False
        elif start[1] == '7':
            if down(start) == end:
                return True
            elif down(down(start)) == end and version[end] == '  ':
                return True
            else:
                print("Invalid move.")
                return False
        elif down(start) == end:
            return True
        else:
            print("Invalid move.")
            return False
    else:
        print("PAWN BLACK HOLE")
        return False

def pawnSwap(end):
    if spaces[end] == 'WP' and end[1] == '8':
        print("""What would you like to exchange your pawn for:
Rook   - enter 'R'
Knight - enter 'N'
Bishop - enter 'B'
Queen  - enter 'Q'""")
        while True:
            newPiece = input()
            if newPiece in pawnSwapPieces:
                spaces[end] = 'W' + newPiece
                break
            else:
                print("Try again:")
                
    elif spaces[end] == 'BP' and end[1] == '1':
        print("""What would you like to exchange your pawn for:
Rook   - enter 'R'
Knight - enter 'N'
Bishop - enter 'B'
Queen  - enter 'Q'""")
        while True:
            newPiece = input()
            if newPiece in pawnSwapPieces:
                spaces[end] = 'B' + newPiece
                break
            else:
                print("Try again:")

    else:
        return None
                
    printBoard(spaces)

def rook(version, start, end):
    if start[0] == end[0]:  # ----- Move UP or DOWN -----
        if start[1] < end[1]:   # Move UP
            start = up(start)
            for _ in range(int(start[1]) + 1, int(end[1]) + 1):
                if version[start] != '  ':   
                    print("Invalid Move.")               
                    return False
                start = up(start)
            return True
        elif start[1] > end[1]: # Move DOWN
            start = down(start)
            for _ in range(int(end[1]) + 1, int(start[1]) + 1):
                if version[start] != '  ':
                    print("Invalid Move.")
                    return False
                start = down(start)
            return True
        else:
            print("Invalid Move.")
            return False
    elif start[1] == end[1]:  # ----- Move RIGHT or LEFT -----
        if ord(start[0]) > ord(end[0]):   # Move LEFT
            start = left(start)
            for _ in range(ord(end[0]) + 1, ord(start[0]) + 1):
                if version[start] != '  ':
                    print("Invalid Move.")
                    return False
                start = left(start)
            return True
        elif ord(start[0]) < ord(end[0]): # Move RIGHT 
            start = right(start)
            for _ in range(ord(start[0]) + 1, ord(end[0]) + 1):
                if version[start] != '  ':   
                    print("Invalid Move.")
                    return False
                start = right(start)
            return True
        else:
            print("Invalid Move.")
            return False
    else:
        print("ROOK BLACK HOLE")
        return False

def knight(start, end):
    if end == upLeft(up(start)):
        return True
    elif end == upRight(up(start)):
        return True
    elif end == upRight(right(start)):
        return True
    elif end == downRight(right(start)):
        return True
    elif end == downRight(down(start)):
        return True
    elif end == downLeft(down(start)):
        return True
    elif end == downLeft(left(start)):
        return True
    elif end == upLeft(left(start)):
        return True
    else:
        print("KNIGHT BLACK HOLE")
        return False
    
def bishop(version, start, end):
    if int(start[1]) < int(end[1]):     # ----- Move UP -----
        if ord(start[0]) > ord(end[0]):     # Move UP-LEFT
            start = upLeft(start)
            for _ in range(int(start[1]) + 1, int(end[1]) + 1):
                if start in version and version[start] != '  ':
                    print("Invalid Move.")
                    return False
                start = upLeft(start)
            if start == end:
                return True
            else:
                print("Invalid Move.")
                return False
        elif ord(start[0]) < ord(end[0]):   # Move UP-RIGHT
            start = upRight(start)
            for _ in range(int(start[1]) + 1, int(end[1]) + 1):
                if start in version and version[start] != '  ':
                    print("Invalid Move.")
                    return False
                start = upRight(start)
            if start == end:
                return True
            else:
                print("Invalid Move.")
                return False
        else:
            print("Invalid Move.")
            return False
    elif int(start[1]) > int(end[1]):   # ----- Move DOWN -----
        if ord(start[0]) > ord(end[0]):     # Move DOWN-LEFT
            start = downLeft(start)
            for _ in range(int(end[1]) + 1, int(start[1]) + 1):
                if start in version and version[start] != '  ':
                    print("Invalid Move.")
                    return False
                start = downLeft(start)
            if start == end:
                return True
            else:
                print("Invalid Move.")
                return False
        elif ord(start[0]) < ord(end[0]):   # Move DOWN-RIGHT
            start = downRight(start)
            for _ in range(int(end[1]) + 1, int(start[1]) + 1):
                if start in version and version[start] != '  ':
                    print("Invalid Move.")
                    return False
                start = downRight(start)
            if start == end:
                return True
            else:
                print("Invalid Move.")
                return False
        else:
            print("Invalid Move.")
            return False
    else:
        print("BISHOP BLACK HOLE")
        return False

def queen(version, start, end):
    if start[0] == end[0] or start[1] == end[1]:
        return rook(version, start, end)
    else:
        return bishop(version, start, end)

def king(start, end):
    if end == up(start):
        return True
    elif end == upRight(start):
        return True
    elif end == right(start):
        return True
    elif end == downRight(start):
        return True
    elif end == down(start):
        return True
    elif end == downLeft(start):
        return True
    elif end == left(start):
        return True
    elif end == upLeft(start):
        return True
    elif tryCastle(start, end):
        return castle(start, end)
    elif tryCastle(start, end) == False:
        return False
    else:
        print("KING BLACK HOLE")
        return False

def tryCastle(begin, dest):
    if spaces[begin] == 'WK' and begin == 'e1':
        if hasMoved('e1') == True:
            print("Your king has moved, you may not castle.")
            return False
        elif dest == 'c1':
            if spaces['d1'] != '  ' or spaces['c1'] != '  ' or spaces['b1'] != '  ':
                print("You may not castle, there are pieces in the way.")
                return False
            elif hasMoved('a1') == False:
                return True
            else:
                print("Your rook has moved. You may not castle.")
                return False
        elif dest == 'g1':
            if spaces['f1'] != '  ' or spaces['g1'] != '  ':
                print("You may not castle, there are pieces in the way.")
                return False
            elif hasMoved('h1') == False:
                return True
            else:
                print("Your rook has moved. You may not castle.")
                return False
        else:
            return False
    if spaces[begin] == 'BK' and begin == 'e8':             #TODO: Double "Your rook has moved"
        if hasMoved('e8') == True:
            print("Your king has moved, you may not castle.")
            return False
        elif dest == 'c8':
            if spaces['d8'] != '  ' or spaces['c8'] != '  ' or spaces['b8'] != '  ':
                print("You may not castle, there are pieces in the way.")
                return False
            elif hasMoved('a8') == False:
                return True
            else:
                print("Your rook has moved. You may not castle.")
                return False
        elif dest == 'g8':
            if spaces['f8'] != '  ' or spaces['g8'] != '  ':
                print("You may not castle, there are pieces in the way.")
                return False
            elif hasMoved('h8') == False:
                return True
            else:
                print("Your rook has moved. You may not castle.")
                return False
        else:
            return False
    else:
        return False

def castle(begin, dest):
    theKing = spaces[begin]
    while attempt[dest] != spaces[begin]:
        if check(attempt, begin) == True:
            print("King is in check, you may not castle.")
            return False
        elif dest[0] == 'c':
            attempt[begin] = '  '
            begin == left(begin)
            attempt[begin] = theKing
        elif dest[0] == 'g':
            attempt[begin] = '  '
            begin == right(begin)
            attempt[begin] = theKing
        else:
            print("Something done fucked up...")
            return False
    if dest == 'c1':
        spaces['d1'] = 'WR'
        spaces['a1'] = '  '
        return True
    elif dest == 'c8':
        spaces['d8'] = 'BR'
        spaces['a8'] = '  '
        return True
    elif dest == 'g1':
        spaces['f1'] = 'WR'
        spaces['h1'] = '  '
        return True
    elif dest == 'g8':
        spaces['f8'] = 'BR'
        spaces['h8'] = '  '
        return True
    else:
        return False

def hasMoved(pieceSpace):               # ???????
    if len(moveList) > 2:
        if spaces[pieceSpace][0] == 'W':
            for i in range(1, len(moveList) + 1):
                if moveList[i][0][0] == pieceSpace:
                    return True
        elif spaces[pieceSpace][0] == 'B':
            for i in range(1, len(moveList)):
                if moveList[i][1][0] == pieceSpace: #TODO: ERROR List out of range
                    return True
        else:
            return False
    return False

def isKing(side):
    for i in attempt.keys():
        if attempt[i] == side + 'K':
                return i
    print("Didn't find a king....")
    return 'False'

def check(version, king):
    with HiddenPrints():
        for i in attempt.keys():
            if attempt[i] != '  ':
                if attempt[i][0] != attempt[king][0]:
                    if chessPiece(version, i, king) == True:
                        return True
        print("Nothing is in check...")
        return False

def checkMate(side, king):
    with HiddenPrints():
        count1 = 0
        count2 = 0
        for i in attempt.keys():
            if attempt[i][0] != side:
                attempt[i] = attempt[king]
                attempt[king] = '  '
                if chessPiece(attempt, king, i) == True:
                    count1 += 1
                    if check(attempt, i) == True:
                        count2 += 1
                attempt[i] = spaces[i]
                attempt[king] = spaces[king]
        if count1 != count2:
            return False
        for i in attempt.keys():
            if attempt[i][0] != side:
                for k in attempt.keys():
                    if attempt[k][0] == side and k != king:
                        if chessPiece(attempt, k, i) == True:
                            attempt[i] = attempt[k]
                            attempt[k] = '  '
                            if check(attempt, king) != True:
                                attempt[i] = spaces[i]
                                attempt[k] = spaces[k]
                                return False
                        attempt[i] = spaces[i]
                        attempt[k] = spaces[k]
        return True


# Running code

pawnSwapPieces = ('R', 'N', 'B', 'Q')
play = 'y'
while play == 'y':
    moveList = {}
    spaces = {'a8': 'BR', 'b8': 'BN', 'c8': 'BB', 'd8': 'BQ', 'e8': 'BK', 'f8': 'BB', 'g8': 'BN', 'h8': 'BR',
              'a7': 'BP', 'b7': 'BP', 'c7': 'BP', 'd7': 'BP', 'e7': 'BP', 'f7': 'BP', 'g7': 'BP', 'h7': 'BP',
              'a6': '  ', 'b6': '  ', 'c6': '  ', 'd6': '  ', 'e6': '  ', 'f6': '  ', 'g6': '  ', 'h6': '  ',
              'a5': '  ', 'b5': '  ', 'c5': 'BN', 'd5': '  ', 'e5': '  ', 'f5': '  ', 'g5': '  ', 'h5': '  ',
              'a4': '  ', 'b4': '  ', 'c4': '  ', 'd4': '  ', 'e4': '  ', 'f4': '  ', 'g4': '  ', 'h4': '  ',
              'a3': '  ', 'b3': '  ', 'c3': '  ', 'd3': '  ', 'e3': '  ', 'f3': '  ', 'g3': '  ', 'h3': '  ',
              'a2': 'WP', 'b2': 'WP', 'c2': 'WP', 'd2': 'WP', 'e2': 'WP', 'f2': 'WP', 'g2': 'WP', 'h2': 'WP',
              'a1': 'WR', 'b1': 'WN', 'c1': 'WB', 'd1': 'WQ', 'e1': 'WK', 'f1': 'WB', 'g1': 'WN', 'h1': 'WR'}
    attempt = copy(spaces)
    printBoard(spaces)
    game()
    play = restart()
