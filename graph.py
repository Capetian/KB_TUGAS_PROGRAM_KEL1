class Graph:
    def __init__(self,state,moves,parent,cost,heuristic):
        self.state = state
        self.moves = moves
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic
        self.fcost = cost + heuristic
        if self.state:
            self.str_map = "".join(str(to_str) for to_str in self.state)
    
    def __eq__(self,other):
        return self.str_map == other.str_map