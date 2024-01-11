"""Script to verify the output solution file.
To run (example):
    python verifyGraph.py small.txt small-soln.txt 
"""
import sys
import re

GRAPH_FILE_NAME = sys.argv[1]
OUTPUT_FILE_NAME = sys.argv[2]
NSIndex, EWIndex = 0, 0  # Movement indices for tracking current node
BullsEye = 'O'

# Get matrix/graph
with open(GRAPH_FILE_NAME) as file:
    next(file)
    graph = [line.split() for line in file]

# Get solution
soln_path_list = open(OUTPUT_FILE_NAME).read().split()

for i in range(len(soln_path_list)):
    # Boundary check for movement indices
    if (NSIndex >= len(graph) or EWIndex >= len(graph[0])) or (
            EWIndex < 0 or NSIndex < 0):
        raise Exception("Index out of graph's boundary")

    node = re.split('(\d+)', soln_path_list[i])
    # Get distance to move
    distance = int(node[1])
    # Get direction to move
    directions = node[2].upper()

    # Check for current path's direction
    current_node = (graph[NSIndex][EWIndex]).upper()
    if current_node != BullsEye:
        curr_color, curr_direction = current_node.split("-")
        if curr_direction != directions:
            print(curr_direction)
            raise Exception("Invalid direction for node provided.")

        # Move across the graph.
        for direction in list(directions):  # Ex: list(NS) -> [N, S]
            if direction == 'N':
                NSIndex -= distance
            elif direction == 'S':
                NSIndex += distance
            elif direction == 'E':
                EWIndex += distance
            elif direction == 'W':
                EWIndex -= distance
            else:
                raise Exception("Unknown direction found.")


# Final movement indices from above will be bullseye if path is correct
final_node = graph[NSIndex][EWIndex].upper()
if final_node == BullsEye:
    print("Path is CORRECT.")
else:
    print("Path is INCORRECT.", final_node)
