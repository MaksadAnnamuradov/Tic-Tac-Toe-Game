from application import Board

def test_winnerIndexes():
    newBoard = Board(1)

    assert set(tuple(w) for w in newBoard.win_indexes())=={
        tuple([(0,0)])
        }

def test_winnerIndexes2():
    newBoard = Board(2)

    assert set(tuple(w) for w in newBoard.win_indexes())=={
            ((0,0),(1,1)),
            ((0,1),(1,1)),
            ((0,0),(1,0)),
            ((1,0),(1,1)),
            ((0,1),(1,0)),
            ((0,0),(0,1))
        }


def test_winnerIndexes3():
    newBoard = Board(3)

    assert set(tuple(w) for w in newBoard.win_indexes())=={
            ((0, 2), (1, 2), (2, 2)),
            ((0, 0), (1, 1), (2, 2)),
            ((0, 2), (1, 1), (2, 0)),
            ((0, 1), (1, 1), (2, 1)),
            ((0, 0), (1, 0), (2, 0)),
            ((0, 0), (0, 1), (0, 2)),
            ((1, 0), (1, 1), (1, 2)),
            ((2, 0), (2, 1), (2, 2))
        }

def test_winnerIndexes4():
    newBoard = Board(4)

    assert set(tuple(w) for w in newBoard.win_indexes())=={
            ((0,0),(0,1),(0,2),(0,3)),
            ((1,0),(1,1),(1,2),(1,3)),
            ((2,0),(2,1),(2,2),(2,3)),
            ((3,0),(3,1),(3,2),(3,3)), #Rows

            ((0,0),(1,0),(2,0),(3,0)),
            ((0,1),(1,1),(2,1),(3,1)),
            ((0,2),(1,2),(2,2),(3,2)),
            ((0,3),(1,3),(2,3),(3,3)), #Cols

            ((0,0),(1,1,),(2,2),(3,3)),
            ((0,3),(1,2,),(2,1),(3,0))
        }

def test_Row3by3():
    newBoard = Board(3)

    newBoard.makeMove(0, 0, "X")
    newBoard.makeMove(0, 1, "X")
    newBoard.makeMove(0, 2, "X") #Row1


    assert newBoard.is_winner("X") == True

def test_Col3by2():
    newBoard = Board(3)

    newBoard.makeMove(0, 2, "Y")
    newBoard.makeMove(1, 2, "Y")
    newBoard.makeMove(2, 2, "Y") #Row1

    assert newBoard.is_winner("Y") == True


def test_Diag1_3by3():
    newBoard = Board(3)

    newBoard.makeMove(0, 0, "Y")
    newBoard.makeMove(1, 1, "Y")
    newBoard.makeMove(2, 2, "Y") #Row1


    assert newBoard.is_winner("Y") == True


def test_Diag2_3by3():
    newBoard = Board(3)

    newBoard.makeMove(0, 2, "X")
    newBoard.makeMove(1, 1, "X")
    newBoard.makeMove(2, 0, "X") #Row1


    assert newBoard.is_winner("X") == True

def test_NotWinner3by3():
    newBoard = Board(3)

    newBoard.makeMove(0, 2, "X")
    newBoard.makeMove(1, 2, "X")
    newBoard.makeMove(2, 1, "X") #Row1


    assert newBoard.is_winner("X") == False


def test_Row4by4():
    newBoard = Board(4)

    newBoard.makeMove(1, 0, "X")
    newBoard.makeMove(1, 1, "X")
    newBoard.makeMove(1, 2, "X")
    newBoard.makeMove(1, 3, "X")


    assert newBoard.is_winner("X") == True


def test_Diag4by4():
    newBoard = Board(4)

    newBoard.makeMove(0, 0, "X")
    newBoard.makeMove(1, 1, "X")
    newBoard.makeMove(2, 2, "X")
    newBoard.makeMove(3, 3, "X")


    assert newBoard.is_winner("X") == True


def test_NotWinner4by4():
    newBoard = Board(4)

    newBoard.makeMove(0, 0, "X")
    newBoard.makeMove(1, 2, "X")
    newBoard.makeMove(2, 3, "X")
    newBoard.makeMove(3, 3, "X")


    assert newBoard.is_winner("X") == False