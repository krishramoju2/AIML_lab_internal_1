import heapq

class Puzzle:
    def __init__(self, start, goal):
        self.start = tuple(start)
        self.goal = tuple(goal)
        self.n = 3

    # Manhattan Distance Heuristic
    def manhattan(self, state):
        dist = 0
        for i in range(len(state)):
            val = state[i]
            if val != 0:
                goal_index = self.goal.index(val)
                x1, y1 = divmod(i, self.n)
                x2, y2 = divmod(goal_index, self.n)
                dist += abs(x1 - x2) + abs(y1 - y2)
        return dist

    # Generate neighbor states
    def neighbors(self, state):
        result = []
        zero = state.index(0)
        x, y = divmod(zero, self.n)

        moves = [(-1,0),(1,0),(0,-1),(0,1)]

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.n and 0 <= ny < self.n:
                new = list(state)
                new_pos = nx * self.n + ny
                new[zero], new[new_pos] = new[new_pos], new[zero]
                result.append(tuple(new))

        return result

    # A* Search
    def solve(self):
        pq = []
        heapq.heappush(pq, (self.manhattan(self.start), 0, self.start, []))

        visited = set()

        while pq:
            f, g, state, path = heapq.heappop(pq)

            if state == self.goal:
                return path

            visited.add(state)

            for nxt in self.neighbors(state):
                if nxt not in visited:
                    new_cost = g + 1
                    priority = new_cost + self.manhattan(nxt)
                    heapq.heappush(pq, (priority, new_cost, nxt, path + [nxt]))

        return None


# Example
start = [1,2,3,4,5,6,7,0,8]
goal = [1,2,3,4,5,6,7,8,0]

p = Puzzle(start, goal)
solution = p.solve()

if solution:
    for step in solution:
        print(step)
else:
    print("No solution found.")
