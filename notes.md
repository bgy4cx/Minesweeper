# Minesweeper

This task is for the yellow belt exam.

## Description

> You are presented with a board of squares. Some squares contain mines (bombs), others don't. If you step
on a square containing a bomb, you lose. If you manage to clear all the squares (without clicking on any
bombs) you win.
Clearing a square which doesn't have a bomb reveals the number of neighbouring squares containing bombs.
If you guess a square contains a bomb mark it with a flag.
A squares "neighbours" are the squares adjacent above, below, left, right, and all 4 diagonals. Squares on the
sides of the board or in a corner have fewer neighbors. The board does not wrap around the edges. If you
clear a square with 0 neighboring bombs, all its neighbors will automatically open; recursively.
The first square you open could be a bomb.
You don't have to mark all the bombs to win; you just need to open all non-bomb squares.

## Notes

 β - Done.
 π - Pomodoro cycle.
 π΄ - Red.
 π’ - Green.
 β»οΈ - Refactor.
 πΏ - Commit.

---

### Guardinas

- Input is a array, a step, flaging option.π΄πΏπ’πΏβ»οΈπΏβπππππππππ
- Output is game board with a message.π΄πΏπ’πΏβ»οΈπΏβπππππππππ

### Process

- To drow a board. π΄πΏπ’πΏβ»οΈπΏβπ
- The player do a step and the code had to check the square if it is a bomb than the game over.π΄πΏπ’πΏβπππππ
- If the square was empty the square shows the number of the bomb(s) in the neighbourhood.π΄πΏπ’πΏβ»οΈπΏβππππ
- The player can remark the squares with a flag where the player assume the bomb.π΄πΏπ’πΏβπππππ
- The empty neighbours have to show theirs emptiness. π΄πΏπ’πΏβ»οΈπΏβπππ
- The player wins if no more empty square on the board. π΄πΏπ’πΏβ»οΈπΏβπππ
