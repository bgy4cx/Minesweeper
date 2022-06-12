from main import drawboard, checkWinner, clearNeighbours, checkBombs, addFlag, doStep

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
    assert clearNeighbours([['_',' ','B'], [' ',' ','B'], ['B','B','B']]) == [['_','_','B'], ['_','_','B'], ['B','B','B']]

def test_clearNeighbours_3():
    assert clearNeighbours([['B','B','B'], ['B',' ',' '], ['B',' ','_']]) == [['B','B','B'], ['B','_','_'], ['B','_','_']]

def test_checkBombs_1():
    assert checkBombs([[' ',' ',' '], [' ','_','_'], [' ','_','B']]) == [[' ',' ',' '], [' ','1','1'], [' ','1','B']]

def test_checkBombs_2():
    assert checkBombs([['B','B','B'], ['B','_','B'], ['B','B','B']]) == [['B','B','B'], ['B','8','B'], ['B','B','B']]

def test_addFlag_1():
    assert addFlag([[' ',' ',' '], [' ',' ',' '], [' ',' ','B']],[1,1]) == [[' ',' ',' '], [' ','F',' '], [' ',' ','B']]

def test_addFlag_2():
    assert addFlag([['B','B','B'], ['B',' ','B'], ['B','B','B']],[0,0]) == [['FB','B','B'], ['B',' ','B'], ['B','B','B']]

def test_doStep_1():
    assert doStep([[' ',' ',' '], [' ',' ',' '], [' ',' ','B']],[1,1]) == [[' ',' ',' '], [' ','_',' '], [' ',' ','B']]

def test_doStep_2():
    assert doStep([['B','B','B'], ['B',' ','B'], ['B','B','B']],[0,0]) == [['X','B','B'], ['B',' ','B'], ['B','B','B']]