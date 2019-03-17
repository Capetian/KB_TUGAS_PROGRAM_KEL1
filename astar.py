from collections import deque
import heapq
from state import State


goal_state = [
    1, 2, 3,
    8, 0, 4,
    7, 6, 5
]
initial_state = [
    2, 8, 3,
    1, 0, 6,
    7, 5, 4
]

queue = [State(initial_state, None, 0, goal_state)]
queue_popped = []

queue_res = deque([])
end_state = None

queue[0].printBoard()

while len(queue):
    now = heapq.heappop(queue)

    isSameBefore = False

    for state in queue_popped:
        if now.isSame(state.board):
            isSameBefore = True
            break

    if isSameBefore:
        continue

    queue_popped.append(now)

    upState = now.expandUp()
    downState = now.expandDown()
    leftState = now.expandLeft()
    rightState = now.expandRight()

    print("OKE " + str(len(queue)))
    if upState is not None:
        #upState.printBoard()
        if upState.isSame(goal_state):
            end_state = upState
            break
        heapq.heappush(queue, upState)
    if downState is not None:
        #downState.printBoard()
        if downState.isSame(goal_state):
            end_state = downState
            break
        heapq.heappush(queue, downState)
    if rightState is not None:
        #rightState.printBoard()
        if rightState.isSame(goal_state):
            end_state = rightState
            break
        heapq.heappush(queue, rightState)
    if leftState is not None:
        #leftState.printBoard()
        if leftState.isSame(goal_state):
            end_state = leftState
            break
        heapq.heappush(queue, leftState)

while end_state is not None:
    queue_res.appendleft(end_state)
    end_state = end_state.parent

step = 1

while len(queue_res):
    print("Step #" + str(step))
    queue_res.popleft().printBoard()
    step += 1

