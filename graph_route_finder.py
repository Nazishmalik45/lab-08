
graph = {
    "S": {"A": 6, "B": 5, "C": 10},
    "A": {"E": 6},
    "B": {"E": 6, "D": 7},
    "C": {"D": 6},
    "D": {"F": 6},
    "E": {"F": 4},
    "F": {"G": 3},
    "G": {}
}

heuristic = {
    "S": 17,
    "A": 10,
    "B": 13,
    "C": 4,
    "D": 2,
    "E": 4,
    "F": 1,
    "G": 0
}

def a_star(start, goal):
    frontier = [(heuristic[start], 0, start, [start])]
    explored = []

    while frontier:
        frontier.sort()
        f, cost, node, path = frontier.pop(0)

        if node in explored:
            continue

        if node == goal:
            print("Path found by A*:", path)
            print("Total cost of this path:", cost)
            print("Nodes explored before goal:", len(explored))
            print("Explored nodes:", explored)
            return path, cost

        explored.append(node)

        for neighbor in graph[node]:
            if neighbor not in explored:
                new_cost = cost + graph[node][neighbor]
                new_f = new_cost + heuristic[neighbor]
                new_path = path + [neighbor]

                frontier.append((new_f, new_cost, neighbor, new_path))
    print("No path found")
    return [], 0

a_star("S", "G")
