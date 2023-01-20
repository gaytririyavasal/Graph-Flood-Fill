
PROJECT DESCRIPTION AND GUIDELINES PROVIDED ON ASSIGNMENT INSTRUCTIONS

In this assignment, you will print the adjacency matrix for a graph and implement Breadth-First Search and Depth-First Search to flood fill pixels in images.

You may also know this feature as ”bucket fill” from graphics applications. It allows you to select a pixel in an image and it will fill the selected pixel and all connected pixels of the same color with a new color, thereby allowing you to change the color of a large area of an image.

You will implement this feature using the Breadth-First Search and Depth-First Search algorithms. We
treat each pixel of an input image as a node in a graph. We start at a given node/pixel and explore the graph from there, changing the color of each pixel as we visit it.

The template reads in a file containing nodes, consisting of an x-&y-coordinate and a color, and edges between the nodes to build a graph. The skeleton code also provides the function ImageGraph.print image () to display the graph of ColorNodes as an image in the console.

In this assignment, your task is to complete a python program with the name GraphFill.py.

Tasks:

You are given the following tasks:

1. Read the code and make sure you understand how the graph is created (don’t worry about the functions at the top of the file; these are helper functions to print out the images).

2. Print the adjacency matrix of the graph.

3. Complete the Breadth-First Search function of the Graph class.

4. Complete the Depth-First Search function of the Graph class.

Rules for the search algorithms:

• Only visit nodes that have the same color as the starting node.
• Color visited nodes in the new color.
• Call the ImageGraph.print image () function after coloring a pixel.

Apart from the ImageGraph and ColorNode classes, you will also find a Stack and a Queue class. You might find these helpful in your search algorithm implementations.

Input:

You will read your input data from the provided *.in files. The file small.in contains the smallest amount of nodes and might be a good starting point to test your implementation. The format of the files will be as follows:

5
5
1, 1, red
2, 1, red
3, 1, red
2, 2, red
3, 2, red
5
0, 1
1, 2
1, 3
2, 4
3, 4
2, green

The first line will be the dimension of the image (width and height). This number is used to initialize the
ImageGraph. The second line is the number of lines following afterwards describing the nodes. Each node
description has the format:

x,y,color.

After the nodes, there’s another line with a single number telling you how many edge descriptions follow.
Each edge description has the format:

from_node_index, to_node_index.

The code template connects from_node to to_node and to_node to from_node.

Finally, there’s a line telling you which node index to start the BFS and DFS algorithms on and which color
to use for the flood fill.

Output:

There’s three parts to the output:

1. The adjacency matrix

2. The intermediate images produced by the BFS algorithm

3. The intermediate images produced by the DFS algorithm

The adjacency matrix has a one at position x,y if there is an edge connecting the node at position x in
the ImageGraph.nodes list and the node at position y in the list; otherwise it is zero in this position. There are
no spaces or other delimiters between the numbers.

Make sure to call ImageGraph.print image () after each pixel that you color and don’t remove the empty print ()
statements that add new lines from the function/add more new lines to the output.

You can additionally find desired outputs for the example *.in files we provided in the out files directory.
Use the print out.py script and pass in one of the *.out files to print the desired outputs in the terminal.
Note that there are multiple ways to traverse the graphs. The grader will accept all correct bfs/dfs imple-
mentations. The example output files show one possible solution that might help you understand what the
expected output should look like.
