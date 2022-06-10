from main import drawboard, checkWinner, clearNeighbours

borad = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]

def test_drawboard_1():
    assert drawboard(borad) == True

def test_drawboard_2():
    assert drawboard([[' ',' ',' '], [' ',' ',' '], [' ',' ']]) == False

def test_checkWinner_1():
    assert checkWinner(borad) == False

def test_checkWinner_2():
    assert checkWinner([['3','B','B'], ['B','B','B'], ['B','B','B']]) == True

def test_clearNeighbours_1():
    assert clearNeighbours([['_',' ',' '], [' ',' ',' '], [' ',' ','B']]) == [['_','_','_'], ['_','_','_'], ['_','_','B']]

def test_clearNeighbours_2():
    assert clearNeighbours([['_',' ','B'], [' ',' ','B'], ['B','B','B']]) == [[['_','_','B'], ['_','_','B'], ['B','B','B']]]