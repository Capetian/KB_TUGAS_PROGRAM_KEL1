from collections import deque


class State:
    indexNull = None
    upState = None
    downState = None
    rightState = None
    leftState = None

    def __init__(self, board, parent, cost, heuristic):
        self.board = board
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

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
                    self.upState = State(new_board, self, self.cost + 1, None)
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
                    self.downState = State(new_board, self, self.cost + 1, None)
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
                    self.rightState = State(new_board, self, self.cost + 1, None)
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
                    self.leftState = State(new_board, self, self.cost + 1, None)
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


goal_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]
initial_state = [2, 8, 3, 1, 6, 4, 7, 5, 0]

queue = deque([State(initial_state, None, 0, None)])
queue_res = deque([])
end_state = None

while len(queue):
    now = queue.popleft()

    upState = now.expandUp()
    downState = now.expandDown()
    leftState = now.expandLeft()
    rightState = now.expandRight()

    if upState is not None:
        if upState.isSame(goal_state):
            end_state = upState
            break
        queue.append(upState)
    if downState is not None:
        if downState.isSame(goal_state):
            end_state = downState
            break
        queue.append(downState)
    if rightState is not None:
        if rightState.isSame(goal_state):
            end_state = rightState
            break
        queue.append(rightState)
    if leftState is not None:
        if leftState.isSame(goal_state):
            end_state = leftState
            break
        queue.append(leftState)

while end_state is not None:
    queue_res.appendleft(end_state)
    end_state = end_state.parent

step = 1

while len(queue_res):
    print("Step #" + str(step))
    queue_res.popleft().printBoard()
    step += 1

