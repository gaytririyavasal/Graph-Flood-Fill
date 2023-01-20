#  File: GraphFill.py

#  Description: The following program prints the adjacency matrix for a graph and uses Breadth-First Search and Depth-First Search to flood fill pixels in images.

#  Student Name: Gaytri Riya Vasal

#  Course Name: CS 313E

#  Unique Number: 86610

#  Date Created: 7/10/2022

#  Date Last Modified: 7/12/2022

import os
import sys

# -----------------------PRINTING LOGIC, DON'T WORRY ABOUT THIS PART----------------------------

# this enables printing colors on Windows somehow
os.system("")

# code to reset the terminal color
RESET_CHAR = "\u001b[0m"
# color codes for the terminal
COLOR_DICT = {
    "black": "\u001b[30m",
    "red": "\u001b[31m",
    "green": "\u001b[32m",
    "yellow": "\u001b[33m",
    "blue": "\u001b[34m",
    "magenta": "\u001b[35m",
    "cyan": "\u001b[36m",
    "white": "\u001b[37m"
}
# character code for a block
BLOCK_CHAR = "\u2588"


# Input: text is some string we want to write in a specific color
#   color is the name of a color that is looked up in COLOR_DICT
# Output: returns the string wrapped with the color code
def colored(text, color):
    color = color.strip().lower()
    if not color in COLOR_DICT:
        raise Exception(color + " is not a valid color!")
    return COLOR_DICT[color] + text


# Input: color is the name of a color that is looked up in COLOR_DICT
# prints a block (two characters) in the specified color
def print_block(color):
    print(colored(BLOCK_CHAR, color) * 2, end='')


# -----------------------PRINTING LOGIC, DON'T WORRY ABOUT THIS PART----------------------------


# Stack class; you can use this for your search algorithms
class Stack(object):
    def __init__(self):
        self.stack = []

    # add an item to the top of the stack
    def push(self, item):
        self.stack.append(item)

    # remove an item from the top of the stack
    def pop(self):
        return self.stack.pop()

    # check the item on the top of the stack
    def peek(self):
        return self.stack[-1]

    # check if the stack if empty
    def is_empty(self):
        return len(self.stack) == 0

    # return the number of elements in the stack
    def size(self):
        return len(self.stack)


# Queue class; you can use this for your search algorithms
class Queue(object):
    def __init__(self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # remove an item from the beginning of the queue
    def dequeue(self):
        return self.queue.pop(0)

    # checks the item at the top of the Queue
    def peek(self):
        return self.queue[0]

    # check if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # return the size of the queue
    def size(self):
        return len(self.queue)


# class for a graph node; contains x and y coordinates, a color, a list of edges and
# a flag signaling if the node has been visited (useful for search algorithms)
# it also contains a "previous color" attribute. This might be useful for your flood fill implementation.
class ColorNode:
    # Input: x, y are the location of this pixel in the image
    #   color is the name of a color
    def __init__(self, index, x, y, color):
        self.index = index
        self.color = color
        self.prev_color = color
        self.x = x
        self.y = y
        self.edges = []
        self.visited = False

    # Input: node_index is the index of the node we want to create an edge to in the node list
    # adds an edge and sorts the list of edges
    def add_edge(self, node_index):
        self.edges.append(node_index)

    # Input: color is the name of the color the node should be colored in;
    # the function also saves the previous color (might be useful for your flood fill implementation)
    def visit_and_set_color(self, color):
        self.visited = True
        self.prev_color = self.color
        self.color = color

        print("Visited node " + str(self.index))


# class that contains the graph
class ImageGraph:
    def __init__(self, image_size):
        self.nodes = []
        self.image_size = image_size
        self.adj_matrix = []

    # prints the image formed by the nodes on the command line
    def print_image(self):
        img = [["black" for i in range(self.image_size)] for j in range(self.image_size)]

        # fill img array
        for node in self.nodes:
            img[node.y][node.x] = node.color

        for line in img:
            for pixel in line:
                print_block(pixel)
            print()
        # print new line/reset color
        print(RESET_CHAR)

    # sets the visited flag to False for all nodes
    def reset_visited(self):
        for i in range(len(self.nodes)):
            self.nodes[i].visited = False

    def get_adj_unvisited_and_color_correct_vertex(self, v, correctcolor):
        nVert = len(self.nodes)
        for i in range(nVert):
            if (self.adj_matrix[v][i] > 0) and (not (self.nodes[i]).visited) and (self.nodes[i].color == correctcolor):
                return i
        return -1

    # implement your adjacency matrix printing here.
    def print_adjacency_matrix(self):

        print("Adjacency matrix:")

        self.adj_matrix = [[0 for x in range(len(self.nodes))] for x in range(len(self.nodes))] # Create matrix with 0s

        for node in self.nodes: # Traverse nodes in for loop
            if len(node.edges) != 0:
                for edge in node.edges: # Traverse each edge in the edges list
                    self.adj_matrix[node.index][edge] = 1 # Change corresponding element to 1

        for row in range(len(self.adj_matrix)): # Traverse rows and columns of adjacency matrix
            for col in range(len(self.adj_matrix[row])):
                print(self.adj_matrix[row][col], end='')
            print('')

        # empty line afterwards
        print()

    # implement your bfs algorithm here. Call print_image() after coloring a node
    # Input: graph is the graph containing the nodes
    #   start_index is the index of the currently visited node
    #   color is the color to fill the area containing the current node with
    def bfs(self, start_index, color):
        
        # reset visited status
        self.reset_visited()
        
        # print initial state
        print("Starting BFS; initial state:")
        self.print_image()

        level_counter = 1 # Set level_counter to 1
        
        # create the Queue to do FIFO
        frontier = Queue()

        level = dict() # Create dictionary for level

        # add the start vertex into the queue
        frontier.enqueue(start_index)
        
        # set the level of start point
        level[start_index] = 0

        self.adj_matrix = [[0 for x in range(len(self.nodes))] for x in range(len(self.nodes))] # Create matrix with 0s

        for node in self.nodes: # Traverse nodes in for loop
            if len(node.edges) != 0:
                for edge in node.edges: # Traverse each edge in the edges list
                    self.adj_matrix[node.index][edge] = 1 # Change corresponding element to 1

        # While frontier is not empty open level by level.
        while not frontier.is_empty():
            
            s = frontier.dequeue() # Dequeue frontier

            # mark the vertex v as visited and push it on the Stack
            if not self.nodes[s].visited: # Check if node has been visited
                
                (self.nodes[s]).visited = True
                (self.nodes[s]).color = color
                prev_node = self.nodes[s]
                print("Visited node " + str(self.nodes[s].index))
                self.print_image()

            next_nodes = [i for i, e in enumerate(self.adj_matrix[s]) if e != 0] # Create list of next nodes to traverse
            
            for vertex in next_nodes: # Go through each node in next_nodes
                
                if not self.nodes[vertex].visited and prev_node.prev_color == self.nodes[vertex].color: # If node has not been visited and has the same color as the previous color
                    
                    print("Visited node " + str(self.nodes[vertex].index))
                    (self.nodes[vertex]).visited = True
                    (self.nodes[vertex]).color = color
                    prev_node = self.nodes[vertex]
                    self.print_image()
                    frontier.enqueue(vertex)
                    level[vertex] = level_counter

            level_counter += 1 # Increment level_counter

        print(level)
        
    # implement your dfs algorithm here. Call print_image() after coloring a node
    # Input: graph is the graph containing the nodes
    #   start_index is the index of the currently visited node
    #   color is the color to fill the area containing the current node with
    def dfs(self, start_index, color):
        
        # reset visited status
        self.reset_visited()
        
        # print initial state
        print("Starting DFS; initial state:")
        self.print_image()

        theStack = Stack() # Create Stack object

        self.adj_matrix = [[0 for x in range(len(self.nodes))] for x in range(len(self.nodes))] # Create matrix with 0s

        for node in self.nodes: # Traverse all nodes
            if len(node.edges) != 0:
                for edge in node.edges: # Traverse all edges
                    self.adj_matrix[node.index][edge] = 1 # Change corresponding element to 1

        color_elim = self.nodes[start_index].prev_color # Store the previous color in color_elim

        # mark the vertex v as visited and push it on the Stack
        (self.nodes[start_index]).visited = True
        (self.nodes[start_index]).color = color
        print("Visited node " + str((self.nodes[start_index]).index))
        self.print_image()

        theStack.push(start_index) # Push start_index on the stack
        time_counter = 1 # Establish time_counter with a value of 1

        finish_times = dict() # Create a dictionary named finish_times
        finish_times[start_index] = time_counter # Change the corresponding element in the dictionary and set value to time_counter

        # visit all the other vertices according to depth
        while not theStack.is_empty():
            
            # get an adjacent unvisited vertex
            u = self.get_adj_unvisited_and_color_correct_vertex(theStack.peek(), color_elim)

            time_counter += 1 # Increment time_counter by 1

            if u == -1: # If u is -1, pop value out of stack and increment time counter
                
                u = theStack.pop()
                time_counter += 1
                
            else: # Otherwise, implement the following:
                
                (self.nodes[u]).visited = True
                (self.nodes[u]).color = color
                print("Visited node " + str((self.nodes[u]).index))
                self.print_image()
                # Add the finishing time for this vertex.
                finish_times[u] = time_counter
                theStack.push(u)

        time_counter += 1

        # the stack is empty, let us rest the flags
        nVert = len(self.nodes)
        
        for i in range(nVert): # Traverse vertices
            (self.nodes[i]).visited = False

        # print(finish_times)

def create_graph(data):
    # creates graph from read in data
    data_list = data.split("\n")

    # get size of image, number of nodes
    image_size = int(data_list[0])
    node_count = int(data_list[1])

    graph = ImageGraph(image_size)

    index = 2

    # create nodes
    for i in range(node_count):
        # node info has the format "x,y,color"
        node_info = data_list[index].split(",")
        new_node = ColorNode(len(graph.nodes), int(node_info[0]), int(node_info[1]), node_info[2])
        graph.nodes.append(new_node)
        index += 1

    # read edge count
    edge_count = int(data_list[index])
    index += 1

    # create edges between nodes
    for i in range(edge_count):
        # edge info has the format "fromIndex,toIndex"
        edge_info = data_list[index].split(",")
        # connect node 1 to node 2 and the other way around
        graph.nodes[int(edge_info[0])].add_edge(int(edge_info[1]))
        graph.nodes[int(edge_info[1])].add_edge(int(edge_info[0]))
        index += 1

    # read search info
    search_info = data_list[index].split(",")
    search_start = int(search_info[0])
    search_color = search_info[1]

    return graph, search_start, search_color

def main():
    # read input
    data = sys.stdin.read()

    graph, search_start, search_color = create_graph(data)

    # print matrix
    graph.print_adjacency_matrix()

    # run bfs
    graph.bfs(search_start, search_color)

    # reset by creating graph again
    graph, search_start, search_color = create_graph(data)

    # run dfs
    graph.dfs(search_start, search_color)


if __name__ == "__main__":
    main()
