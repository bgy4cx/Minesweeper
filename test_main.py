from main import drawboard

borad = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]

def test_drawboard():
    assert drawboard(borad) == True

def test_drawboard():
    assert drawboard([[' ',' ',' '], [' ',' ',' '], [' ',' ']]) == False
