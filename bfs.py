from collections import deque
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

queue = deque([State(initial_state, None, 0, goal_state)])
queue_popped = []
queue_res = deque([])
end_state = None

time = 0

while len(queue):
    time += 1
    now = queue.popleft()

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

step = 0

while len(queue_res):
    print("Step #" + str(step))
    queue_res.popleft().printBoard()
    step += 1

print("Jumlah Loop\t\t: " + str(time))
print("Jumlah State di Queue\t: " + str(len(queue)))
