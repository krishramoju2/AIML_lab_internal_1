import heapq 
 
class Node: 
    def __init__(self, position, parent=None): 
        self.position = position 
        self.parent = parent 
        self.g = 0  # Cost from start to current node 
        self.h = 0  # Heuristic cost estimate to goal 
        self.f = 0  # Total cost
 
    def __lt__(self, other): 
        return self.f < other.f 
 
def heuristic(a, b): 
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) 
 
def a_star_algorithm(grid, start, goal): 
    open_list = [] 
    closed_list = set() 
     
    start_node = Node(start) 
    goal_node = Node(goal) 
     
    heapq.heappush(open_list, start_node) 
     
    while open_list: 
        current_node = heapq.heappop(open_list) 
        closed_list.add(current_node.position) 
         
        # Goal reached 
        if current_node.position == goal_node.position: 
            path = [] 
            while current_node: 
                path.append(current_node.position) 
                current_node = current_node.parent 
            return path[::-1]  # Return reversed path 
         
        # Generate neighbors (up, down, left, right) 
        neighbors = [(0, -1), (0, 1), (-1, 0), (1, 0)] 
        for new_position in neighbors: 
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + 
new_position[1]) 
             
            if (node_position[0] > (len(grid) - 1) or  
                node_position[0] < 0 or  
                node_position[1] > (len(grid[0]) - 1) or  
                node_position[1] < 0): 
                continue 
             
            if grid[node_position[0]][node_position[1]] != 0: 
                continue 
 
            neighbor = Node(node_position, current_node) 
            if neighbor.position in closed_list: 
                continue 
 
            neighbor.g = current_node.g + 1 
            neighbor.h = heuristic(neighbor.position, goal_node.position) 
            neighbor.f = neighbor.g + neighbor.h 
             
            if add_to_open(open_list, neighbor):










                                heapq.heappush(open_list, neighbor) 
 
    return None 
 
def add_to_open(open_list, neighbor): 
    for node in open_list: 
        if neighbor.position == node.position and neighbor.g > node.g: 
            return False 
    return True 
 
# Example grid (0 = open, 1 = obstacle) 
grid = [ 
    [0, 1, 0, 0, 0, 0], 
    [0, 0, 0, 1, 1, 0], 
    [0, 0, 0, 1, 0, 0], 
    [0, 1, 1, 0, 0, 0], 
    [0, 1, 0, 0, 0, 0], 
    [0, 0, 1, 0, 0, 0] 
] 
 
start = (0, 0) 
goal = (5, 5) 
 
path = a_star_algorithm(grid, start, goal) 
print("Path:", path)
