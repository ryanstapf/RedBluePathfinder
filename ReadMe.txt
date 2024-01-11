You must traverse a matrix of arrows (red or blue). You must find a route from the arrow in the
top left corner to the bullseye in the bottom right corner. You must follow the direction that the
arrows point, and you can only stop on the other colored arrow or the bullseye. For example, start
on red, then chose a blue arrow (in the direction that the red arrow is pointing), then from the blue
arrow chose a red arrow in the direction the blue arrow is pointing. Continue in this fashion until
you find the bullseye in the bottom right c orner. It does not have to be the first opposite color that
you find. You may find your-self in a loop and continuously vi siting the same ar rows; you need
to account for this. You must find the correct p a th. You also need to handle what happens if you
get to a node that you already visited within a path and you need to continue in that direction.

This A* algorithm determines this path by backtracking when a dead end or cycle is detected.

The command line arguments are the file name (Project2.py), the graph name (ex. medium.txt), and the name of the solution (ex. medium-soln.txt).

You may also verify the solution with the verifyGraph.py file and the same command line arguments as above.