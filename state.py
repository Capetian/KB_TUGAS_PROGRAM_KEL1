import math

class State:
    TYPE_BOARD_NOW = 0
    TYPE_BOARD_GOAL = 1

    posBoard = None
    posGoal_Board = None
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
        for idx, val in enumerate(self.board):
            if val != otherBoard[idx]:
                return False
        return True

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
            for val in self.board:
                posNow = self.getPos(self.TYPE_BOARD_NOW, val)
                posGoal = self.getPos(self.TYPE_BOARD_GOAL, val)
                posNow_x = posNow % 3 + 1
                posNow_y = math.ceil(posNow / 3)
                posGoal_x = posGoal % 3 + 1
                posGoal_y = math.ceil(posGoal / 3)
                diff += abs(posNow_x - posGoal_x) + abs(posNow_y - posGoal_y)
            self.heuristic = diff
        return self.heuristic
        # if self.heuristic is None:
        #     diff = 0
        #     for idx, val in enumerate(self.board):
        #         if val != goalBoard[idx]:
        #             diff += 1
        #     self.heuristic = diff
        # return self.heuristic

    def getPos(self, type, number):
        if type == self.TYPE_BOARD_NOW:
            if self.posBoard is None:
                self.posBoard = [None, None, None, None, None, None, None, None, None]
                for idx, val in enumerate(self.board):
                    self.posBoard[val] = idx
            return self.posBoard[number]
        elif type == self.TYPE_BOARD_GOAL:
            if self.posGoal_Board is None:
                self.posGoal_Board = [None, None, None, None, None, None, None, None, None]
                for idx, val in enumerate(self.goal_board):
                    self.posGoal_Board[val] = idx
            return self.posGoal_Board[number]
        return None

    def __lt__(self, other):
        """
        :type other: State
        """
        return self.cost + self.getHeuristic(self.goal_board) < other.cost + other.getHeuristic(self.goal_board)
