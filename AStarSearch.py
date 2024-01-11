# Intro to Theory of Algorithms: Project 2
#
# Student Name: Ryan Stapf
# Date: 12/1/2023
#

# My program utilizes an A-Star Algorithm to traverse the graph of colored arrows and return the path leading to the goal node.

# An A* algorithm is a graph algorithm based off of Dijkstra's Algorithm that is useful for finding the optimal path between 2 points in a graph. I will briefly describe how it works.

# 1. A priority queue is initialized with the starting node and its associated cost.
# 2. While the PQ is not empty, it repeats the following steps:

    # 1) Pop and return the node with the lowest cost from the PQ.
    # 2) Check if the returned node is the goal node.
    # 3) Generate the adjacent nodes to the current node that can be reached.
    # 4) Evaluate the neighboring nodes by calculating the cost to reach that node and a heuristic estimate of the remaining cost to reach the goal node from that neighbor.
    # 5) Update the total costs of each neighbor.

# 3. Repeat the above until the goal node is found.
# 4. Once the goal node is found, terminate the algorithm and return the path to the goal node.

#===========================================================================================================================================================================================

# Library used for command line argument implementation of input and output files.
import sys

# Library used for priority queue class implementation.
import heapq



# Check if the specified index in the path corresponds to a direction ('N', 'S', 'E', 'W').
def checkDirection(path, i):
    
    if path[i:i + 1] == 'N':
        return True
    elif path[i:i + 1] == 'S':
        return True
    elif path[i:i + 1] == 'E':
        return True
    elif path[i:i + 1] == 'W':
        return True

    return False



# Calculate the cost of a single action based on the number of steps and cardinal direction.
def actionCost(single_action):
    cost = 0
    backspace = -2

    # Find the starting index of the cardinal direction in reverse order
    while checkDirection(single_action, backspace):
        backspace -= 1
    
    # Extract the number of steps and convert it to an integer
    cost = int(single_action[:backspace + 1])
    return cost



# Calculate the total cost of a sequence of actions.
def totalActionCost(actions):
    cost = 0
    for action in actions:
        cost += actionCost(action)
    return cost



# Determine the row and column increments based on the direction in a node.
# Regardless of whether the direction is cardinal or intermediate, this function outputs the traversal according to row and column.
# For example, if the node direction is SW, it reads S and sets row = 1, and then reads W and sets col = -1 and returns both values 
# resulting in the correct traversal.
def traversal(node):
    row = 0
    col = 0
    directions = node[2:]

    for direction in directions:

        # Update row and/or column based on the direction
        if direction == 'N':
            row = -1
        if direction == 'E':
            col = 1
        if direction == 'S':
            row = 1
        if direction == 'W':
            col = -1

    return row, col



# Pirority Queue data structure object class to be used within the A* algorithm which is defined later.
# The structure of the PQ is based on a heap.
class PriorityQueue:

    def  __init__(self):
        self.heap = []
        self.count = 0
 
    # Append an item to the PQ and specify its priority which determines its position in the queue
    def push(self, item, priority):
        entry = (priority, self.count, item)
        heapq.heappush(self.heap, entry)
        self.count += 1
 
    # Remove an item from the PQ
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty priority queue")
        (_, _, item) = heapq.heappop(self.heap)
        return item
 
    # Return whether or not PQ is empty
    def is_empty(self):
        return len(self.heap) == 0



# Calculate the heuristic for the A* search based on Manhattan distance between two points.
def getHeuristic(start, end):
    heuristic = abs(start[0] - end[0]) + abs(start[1] + end[1])
    return heuristic



# Primary A* Search algorithm to find the optimal path from the starting position to the goal position.
def AS_Search(arrowField, row, col):
    
    # Initialize a priority queue from the PQ class defined earlier.
    # Each value in the PQ will contain the node position and the directions taken to reach that node.
    # The sum of the heuristic value and total action cost will act as the priority value.
    P_Queue = PriorityQueue()
    starting_direction = []
    starting_position = (0, 0)

    # Push the starting position and an empty list of starting directions onto the priority queue.
    P_Queue.push((starting_position, starting_direction), 0)

    # Define the goal position of node "O"
    goal_position = (row - 1, col - 1)

    while not P_Queue.is_empty():
        # Obtain the current position from the front of the priority queue and analyze the x and y coordinates.
        currentPosition, path_obtained = P_Queue.pop()
        x = currentPosition[0]
        y = currentPosition[1]

        # Check if the goal is reached. If so, return the path generated from the starting node to the goal node.
        if x == goal_position[0] and y == goal_position[1]:
            print(path_obtained)
            return path_obtained
        
        # Extract row and column increments based on the value at x and y in the arrow field 
        # and initialize travelDistance and travelDirection which will be manipulated in the while loop.
        row_inc, col_inc = traversal(arrowField[x][y])
        travel_distance = 0
        travel_direction = (arrowField[x][y])[2:]
        color = (arrowField[x][y])[0]

        # The while loop ensures that the traversal remains in bounds.
        while (x >= 0 and x < len(arrowField)) and (y >= 0 and y < len(arrowField[0])):

            # Check if the color changes. If so, calculate the new position, distance traveled, direction traversed in,
            # heuristic, and update the priority queue.
            if color != (arrowField[x][y])[0]:
                new_position = (x, y)
                distance_direction = "{0}{1}".format(travel_distance, travel_direction)
                path_list = path_obtained + [distance_direction]
                heuristic = getHeuristic(new_position, goal_position)
                
                # Push the new position of the pivot node onto the PQ.
                # Update the PQ with the new postion and the path list,
                # considering the heuristic and total action cost being used as the priority value.
                P_Queue.push((new_position, path_list), heuristic + totalActionCost(path_obtained))

            # Increment the travel distance value by one and increment x and y based on the given direction during the traversal.
            travel_distance += 1
            x += row_inc
            y += col_inc



# Main function. Parses the input text file into a 2D array, calls the A* search algorithm, and writes that data to an output file.
def main():

    # Open and read the input file
    inputFile = open(sys.argv[1], 'r')

    # Read the first line to obtain the dimensions of the arrow field
    inputVal = inputFile.readline().strip()
    HeightByWidth = inputVal.split()
    HeightByWidth = [int(numeric_string) for numeric_string in HeightByWidth]

    # Obtain the dimensions of the array
    height = HeightByWidth[0]
    width = HeightByWidth[1]

    # Initialize the arrow field as an empty array and append all the directional values as strings
    arrowField = []

    while inputVal != '':
        inputVal = inputFile.readline().strip()
        inputSplit = inputVal.split()
        arrowField.append(inputSplit)
    arrowField.pop()

    # Obtain the correct path to the goal node with the A* Search algorithm
    output_path = AS_Search(arrowField, height, width)

    # Write the output path to an output file
    outputFile = open(sys.argv[2], 'w')
    outputFile.write(" ".join(output_path))

    # Close both the input and output files
    outputFile.close()
    inputFile.close()



# Call the main function and execute the program.
main()



# TO GRADER: I was unable to obtain an output for large.txt due to a memory error. However, this algorithm output solutions for tiny.txt, small.txt, and rect.txt