from collections import deque
import heapq 
import itertools
from graph import Graph



def BFS(start, goal):
    visited = set()
    queue = deque([Graph(start,None,None,0,0)])

    while queue:
        curr = queue.popleft()
        visited.add(curr.str_map)
        
        if curr.state == goal:
            return curr
        
        children = expand(curr)

        for next in children:
            if next.str_map not in visited: 
                queue.append(next)
                visited.add(next.str_map)
                

# def AStar(start,goal):
#     visited = set()
#     root = Graph(start,None,None,0,h(start))
#     node_data = ()
#     while pqueue:
#         curr = pqueue.popleft()
        
#         if curr.state == goal_state:
#             return curr
        
#         children = expand(curr)

#         for next in children:
#             if next.map not in visited: 
#                 queue.append(next)
#                 visited.add(next.str_map)
    

# def h(start):



def moves(curr,dir):
    moved = curr[:]
    i = curr.index(0)

    if dir == 'left':
        if i not in range(0,6,3):
            temp = moved[i - 1]
            moved[i - 1]= moved[i]
            moved[i] = temp

            return moved
        else:
            return None

    if dir == 'up':
        if i not in range(0,3):
            temp = moved[i - 3]
            moved[i - 3]= moved[i]
            moved[i] = temp
            
            return moved
        else:
            return None

    if dir == 'right':
        if i not in range(2,8,3):
            temp = moved[i + 1]
            moved[i + 1]= moved[i]
            moved[i] = temp
            
            return moved
        else:
            return None

    if dir == 'down':
        if i not in range(6,8):
            temp = moved[i + 3]
            moved[i + 3]= moved[i]
            moved[i] = temp
            
            return moved
        else:
            return None
    
def expand(curr):
    
    child = list()

    child.append(Graph(moves(curr.state, 'left'),'left', curr, curr.cost + 1 , 0))
    child.append(Graph(moves(curr.state, 'up'), 'up', curr, curr.cost + 1 , 0))
    child.append(Graph(moves(curr.state, 'right'), 'right', curr, curr.cost + 1 , 0))
    child.append(Graph(moves(curr.state, 'down'), 'down', curr, curr.cost + 1 , 0))

    expanded = [ i for i in child if i.state]

    return expanded


def sol(end,start):

    curr = end
    solution = list()

    while curr.state != start:
        if curr.moves == 'left':
            solution.insert(0,'left')
        elif curr.moves == 'up':
            solution.insert(0,'up')
        elif curr.moves == 'right':
            solution.insert(0,'right')
        else:
            solution.insert(0,'down')
        curr = end_node.parent

    return solution


goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
initial_state = [1, 0, 2, 3, 4, 5, 6, 7, 8]
end_node = BFS(initial_state, goal_state)
solution = sol(end_node, initial_state)
for i in solution:
    print(i) 




