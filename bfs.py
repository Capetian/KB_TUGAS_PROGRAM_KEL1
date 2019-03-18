from collections import deque
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

queue = deque([State(initial_state, None, 0, goal_state)])
queue_popped = []
queue_res = deque([])
end_state = None
maxDepth = 0
while len(queue):
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
        if upState.cost > maxDepth:
            maxDepth = upState.cost
        queue.append(upState)
    if downState is not None:
        if downState.isSame(goal_state):
            end_state = downState
            break
        if downState.cost > maxDepth:
            maxDepth = downState.cost
        queue.append(downState)
    if rightState is not None:
        if rightState.isSame(goal_state):
            end_state = rightState
            break
        if rightState.cost > maxDepth:
            maxDepth = rightState.cost
        queue.append(rightState)
    if leftState is not None:
        if leftState.isSame(goal_state):
            end_state = leftState
            break
        if leftState.cost > maxDepth:
            maxDepth = leftState.cost
        queue.append(leftState)



while end_state is not None:
    queue_res.appendleft(end_state)
    end_state = end_state.parent

step = 1
print("Jumlah langkah yang ditelusuri: " + str(len(queue)) ) 
print("Maximum Depth " + str(maxDepth) )
print("Jumlah langkah solusi " + str(len(queue_res) - 1) )  
print("Solusi: ") 
while len(queue_res):
    print("Step #" + str(step))
    queue_res.popleft().printBoard()
    step += 1

