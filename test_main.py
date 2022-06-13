from main import drawboard, checkWinner, clearNeighbours, checkBombs, addFlag, doStep, minesweeper

borad = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]

def test_drawboard_1():
    assert drawboard(borad) == True

def test_drawboard_2():
    assert drawboard([[' ',' ',' '], [' ',' ',' '], [' ',' ']]) == False

def test_drawboard_3():
    assert drawboard([['FB',' ',' '], [' ',' ',' '], [' ',' ',' ']]) == True

def test_drawboard_4():
    assert drawboard([['B',' ',' '], [' ',' ',' '], [' ',' ',' ']]) == True

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

def test_clearNeighbours_4():
    assert clearNeighbours([['B',' ',' '], [' ','B',' '], [' ','_','B']]) == [['B','_','_'], ['_','B','_'], ['_','_','B']]

def test_clearNeighbours_5():
    assert clearNeighbours([['B','_',' '], [' ','B',' '], [' ',' ','B']]) == [['B','_','_'], ['_','B','_'], ['_','_','B']]

def test_clearNeighbours_6():
    assert clearNeighbours([[' ',' ',' '], [' ','B',' '], [' ','_',' ']]) == [['_','_','_'], ['_','B','_'], ['_','_','_']]

def test_checkBombs_1():
    assert checkBombs([[' ',' ',' '], [' ','_','_'], [' ','_','B']]) == [[' ',' ',' '], [' ','1','1'], [' ','1','B']]

def test_checkBombs_2():
    assert checkBombs([['B','B','B'], ['B','_','B'], ['B','B','B']]) == [['B','B','B'], ['B','8','B'], ['B','B','B']]

def test_checkBombs_3():
    assert checkBombs([[' ',' ',' '], [' ','_','_'], [' ','_','FB']]) == [[' ',' ',' '], [' ','1','1'], [' ','1','FB']]

def test_checkBombs_4():
    assert checkBombs([['FB','_','_'], ['_','_','_'], ['_','_','FB']]) == [['FB','1','_'], ['1','2','1'], ['_','1','FB']]

def test_checkBombs_5():
    assert checkBombs([['_','_','_'], ['_','B','_'], ['_','_','_']]) == [['1','1','1'], ['1','B','1'], ['1','1','1']]

def test_checkBombs_6():
    assert checkBombs([['_','_','FB'], ['_','_','_'], ['FB','_','_']]) == [['_','1','FB'], ['1','2','1'], ['FB','1','_']]

def test_checkBombs_7():
    assert checkBombs([['FB','FB','FB'], ['FB','_','FB'], ['FB','FB','FB']]) == [['FB','FB','FB'], ['FB','8','FB'], ['FB','FB','FB']]

def test_checkBombs_8():
    assert checkBombs([['FB','_','FB'], ['_','_','_'], ['FB','_','FB']]) == [['FB','2','FB'], ['2','4','2'], ['FB','2','FB']]

def test_checkBombs_9():
    assert checkBombs([['B','_','B'], ['_','_','_'], ['B','_','B']]) == [['B','2','B'], ['2','4','2'], ['B','2','B']]

def test_checkBombs_10():
    assert checkBombs([['B','B','B'], ['_','_','_'], ['B','B','B']]) == [['B','B','B'], ['4','6','4'], ['B','B','B']]

def test_checkBombs_11():
    assert checkBombs([['_','_','_'], ['B','B','B'], ['_','_','_']]) == [['2','3','2'], ['B','B','B'], ['2','3','2']]

def test_addFlag_1():
    assert addFlag([[' ',' ',' '], [' ',' ',' '], [' ',' ','B']],[1,1]) == [[' ',' ',' '], [' ','F',' '], [' ',' ','B']]

def test_addFlag_2():
    assert addFlag([['B','B','B'], ['B',' ','B'], ['B','B','B']],[0,0]) == [['FB','B','B'], ['B',' ','B'], ['B','B','B']]

def test_addFlag_3():
    assert addFlag([['F',' ',' '], [' ',' ',' '], [' ',' ','B']],[0,0]) == [[' ',' ',' '], [' ',' ',' '], [' ',' ','B']]

def test_addFlag_4():
    assert addFlag([[' ',' ',' '], [' ',' ',' '], [' ',' ','FB']],[2,2]) == [[' ',' ',' '], [' ',' ',' '], [' ',' ','B']]

def test_doStep_1():
    assert doStep([[' ',' ',' '], [' ',' ',' '], [' ',' ','B']],[1,1]) == [[' ',' ',' '], [' ','_',' '], [' ',' ','B']]

def test_doStep_2():
    assert doStep([['B','B','B'], ['B',' ','B'], ['B','B','B']],[0,0]) == [['X','B','B'], ['B',' ','B'], ['B','B','B']]

def test_doStep_3():
    assert doStep([['B','B','B'], ['B',' ','B'], ['B','B','B']],[1,1]) == [['B','B','B'], ['B','_','B'], ['B','B','B']]

def test_minesweeper_1():
    assert minesweeper([['B','B','B'], ['B',' ','B'], ['B','B','B']],"S",[1,1]) == "Win"

def test_minesweeper_2():
    assert minesweeper([['B','B','B'], ['B',' ','B'], ['B','B','B']],"S",[0,0]) == "Lose"

def test_minesweeper_3():
    assert minesweeper([[' ',' ',' '], [' ',' ',' '], [' ',' ','B']],"S",[1,1]) == "Win"

def test_minesweeper_4():
    assert minesweeper([[' ',' ',' '], ['B','B','B'], [' ',' ','B']],"S",[2,1]) == "Next"

def test_minesweeper_5():
    assert minesweeper([[' ',' ',' '], ['B','B','B'], ['_','_','B']],"F",[2,2]) == "Next"

def test_minesweeper_6():
    assert minesweeper([[' ',' ',' '], ['B','B','B'], ['_','_','B']],"F",[0,0]) == "Next"
