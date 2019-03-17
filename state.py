class State:
    indexNull = None
    heuristic = None
    upState = None
    downState = None
    rightState = None
    leftState = None

    def __init__(self, board, parent, cost, goal_board):
        self.board = board
        self.parent = parent
        self.cost = cost
        self.goal_board = goal_board

    def expandUp(self):
        """
        :rtype: State
        """
        if self.upState is None:
            new_board = self.board[:]
            idx = self.getNullIndex()
            if idx not in [0, 1, 2]:
                new_board[idx], new_board[idx - 3] = new_board[idx - 3], new_board[idx]
                if self.isSameAsParent(new_board) is False:
                    self.upState = State(new_board, self, self.cost + 1, self.goal_board)
        return self.upState

    def expandDown(self):
        """
        :rtype: State
        """
        if self.downState is None:
            new_board = self.board[:]
            idx = self.getNullIndex()
            if idx not in [6, 7, 8]:
                new_board[idx], new_board[idx + 3] = new_board[idx + 3], new_board[idx]
                if self.isSameAsParent(new_board) is False:
                    self.downState = State(new_board, self, self.cost + 1, self.goal_board)
        return self.downState

    def expandRight(self):
        """
        :rtype: State
        """
        if self.rightState is None:
            new_board = self.board[:]
            idx = self.getNullIndex()
            if idx not in [2, 5, 8]:
                new_board[idx], new_board[idx + 1] = new_board[idx + 1], new_board[idx]
                if self.isSameAsParent(new_board) is False:
                    self.rightState = State(new_board, self, self.cost + 1, self.goal_board)
        return self.rightState

    def expandLeft(self):
        """
        :rtype: State
        """
        if self.leftState is None:
            new_board = self.board[:]
            idx = self.getNullIndex()
            if idx not in [0, 3, 6]:
                new_board[idx], new_board[idx - 1] = new_board[idx - 1], new_board[idx]
                if self.isSameAsParent(new_board) is False:
                    self.leftState = State(new_board, self, self.cost + 1, self.goal_board)
        return self.leftState

    def getNullIndex(self):
        if self.indexNull is None:
            for idx, val in enumerate(self.board):
                if val == 0:
                    self.indexNull = idx
                    break
        return self.indexNull

    def isSameAsParent(self, newBoard):
        if self.parent is not None:
            return self.isSame(newBoard)
        return False

    def isSame(self, otherBoard):
        same = True
        for idx, val in enumerate(self.board):
            if val != otherBoard[idx]:
                return False
        return same

    def printBoard(self):
        i = 0
        for x in range(0,3):
            for y in range(0,3):
                print(str(self.board[i]), end=" ")
                i += 1
            print(end="\n")
        print(end="\n")

    def getHeuristic(self, goalBoard):
        if self.heuristic is None:
            diff = 0
            for idx, val in enumerate(self.board):
                if val != goalBoard[idx]:
                    diff += 1
            self.heuristic = diff
        return self.heuristic

    def __lt__(self, other):
        """
        :type other: State
        """
        return self.getHeuristic(self.goal_board) < other.getHeuristic(self.goal_board)

