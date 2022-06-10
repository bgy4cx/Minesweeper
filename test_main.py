from main import drawboard, checkWinner

borad = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]

def test_drawboard_1():
    assert drawboard(borad) == True

def test_drawboard_2():
    assert drawboard([[' ',' ',' '], [' ',' ',' '], [' ',' ']]) == False

def test_checkWinner_1():
    assert checkWinner(borad) == False

def test_checkWinner_2():
    assert checkWinner([['3','B','B'], ['B','B','B'], ['B','B','B']]) == True
