from collections import deque
import heapq
from state import State


goal_state = [
    1, 2, 3,
    8, 0, 4,
    7, 6, 5
]
initial_state = [
    1, 0, 3,
    2, 5, 4,
    8, 7, 6
]

queue = [State(initial_state, None, 0, goal_state)]
queue_popped = []

queue_res = deque([])
end_state = None

time = 0

while len(queue):
    time += 1
    now = heapq.heappop(queue)

    # Untuk Syarat Page 27 solution.pdf
    if now.isSame(goal_state):
        end_state = now
        break

    # Untuk Syarat Page 10 solution.pdf
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

    # Untuk Syarat Page 8 solution.pdf
    for idx, state in enumerate(queue):
        if upState is not None and upState.isSame(state.board) and upState.__lt__(state):
            queue[idx] = upState
        if downState is not None and downState.isSame(state.board) and downState.__lt__(state):
            queue[idx] = downState
        if leftState is not None and leftState.isSame(state.board) and leftState.__lt__(state):
            queue[idx] = leftState
        if rightState is not None and rightState.isSame(state.board) and rightState.__lt__(state):
            queue[idx] = rightState

    if upState is not None:
        #upState.printBoard()
        heapq.heappush(queue, upState)
    if downState is not None:
        #downState.printBoard()
        heapq.heappush(queue, downState)
    if rightState is not None:
        #rightState.printBoard()
        heapq.heappush(queue, rightState)
    if leftState is not None:
        #leftState.printBoard()
        heapq.heappush(queue, leftState)

while end_state is not None:
    queue_res.appendleft(end_state)
    end_state = end_state.parent

step = 0

while len(queue_res):
    print("Step #" + str(step))
    queue_res.popleft().printBoard()
    step += 1

print("Jumlah Loop\t\t: " + str(time))
print("Jumlah State di Queue\t: " + str(len(queue)))
