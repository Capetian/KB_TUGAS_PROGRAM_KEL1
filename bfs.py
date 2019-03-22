from collections import deque
from state import State


goal_state = [
    0,1,2,
    3,4,5,
    6,7,8
]
initial_state = [
    7,2,4,
    5,0,6,
    8,3,1
]

queue = deque([State(initial_state, None, 0, goal_state)])
queue_popped = []
queue_res = deque([])
end_state = None

time = 0

maxDepth = 0
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

step = 0

print("Jumlah Loop\t\t\t: " + str(time))
print("Jumlah langkah yang ditelusuri\t: " + str(len(queue)) ) 
print("Maximum Depth\t\t\t: " + str(maxDepth) ) 
print("Jumlah langkah solusi\t\t: " + str(len(queue_res) - 1) ) 
print("\nSolusi: \n") 

while len(queue_res):
    print("Step #" + str(step))
    queue_res.popleft().printBoard()
    step += 1

