#!/usr/bin/python3
"""
Module 101-nqueens
Class that prints solutions to the N queens problem
"""

import sys


class Board:
    """Chess board"""

    queen_sym = 'Q'
    empty_sym = '#'

    def __init__(self, queens):
        self.queens = queens
        self.board = Board.getNewBoard(queens)

    @property
    def board(self):
        """Getter - The board property."""
        return self._board

    @board.setter
    def board(self, value):
        """Setter - set the board property."""
        self._board = value

    @property
    def queens(self):
        """The queens property."""
        return self._queens

    @queens.setter
    def queens(self, value):
        if (not isinstance(value, int)):
            raise TypeError("N must be a number")
        if (value < 4):
            raise TypeError("N must be at least 4")
        self._queens = value

    @staticmethod
    def getNewBoard(size=1):
        """Get a square, empty board matrix size x size

        Args:
            size: square dimensions of board

        Raises:
            TypeError: if size is not an int or less than 0
        """
        if (not isinstance(size, int)):
            raise TypeError("size must be an integer")
        if (size < 1):
            raise TypeError("size must be >= 1")
        return [[False for _ in range(size)] for _ in range(size)]

    def _isSafe(self, r, c):
        """Check if it is safe to place queen in board[r][c]

        Args:
            r: board row
            c: board column
        """
        for i in range(r):
            if self.board[i][c]:
                return False
        (i, j) = (r, c)
        while i >= 0 and j >= 0:
            if self.board[i][j]:
                return False
            i -= 1
            j -= 1
        (i, j) = (r, c)
        while i >= 0 and j < self.queens:
            if self.board[i][j]:
                return False
            i -= 1
            j += 1
        return True

    def nQueen(self, r):
        """Backtrack in placing queens on board

        Args:
            r: current row being tested
        """
        if r == self.queens:
            print(str(Board.getIndexes(self.board)))
            return

        # place queen at every square in the current row `r`
        # and recur for each valid movement
        for i in range(self.queens):
            # if no two queens threaten each other
            if self._isSafe(r, i):
                # place queen on the current square
                self.board[r][i] = True

                # recur for the next row
                self.nQueen(r + 1)

                # backtrack and remove the queen from the current square
                self.board[r][i] = False

    @staticmethod
    def getIndexes(board):
        """Represent the board as spots with a chess piece

        Args:
            board: The mask value of the board
        """
        _board = []
        for i, r in enumerate(board):
            for j, c in enumerate(r):
                if (c):
                    _board.append([i, j])
        return _board

    def __str__(self):
        _str = ''
        for r in self.board:
            for c in r:
                _str += f'{c and self.queen_sym or self.empty_sym} '
            _str += '\n'
        return _str.strip()

    def __repr__(self):
        return f'Board({self.queens})'


if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        board = Board(n)
    except ValueError as e:
        print("N must be a number")
        sys.exit(1)
    except Exception as e:
        print(e)
        sys.exit(1)
    else:
        board.empty_sym = '-'
        board.nQueen(0)
