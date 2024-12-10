import graphviz
from graphviz import Digraph
import numpy as np

P = complex

input_file = open("./input.txt", "r")

lines = input_file.read().split("\n")

input_file.close()


def p_to_xy(dir):
    return int(dir.real), int(dir.imag)


grid = []
trailheads = []

for row, line in enumerate(lines):
    curr_line = []
    for col, c in enumerate(line):
        curr_line.append(int(c))
        if c == "0":
            trailheads.append(P(col, row))

    grid.append(np.array(curr_line))

grid = np.array(grid)


class Node:
    def __init__(self, value, row, col):
        self.value = value
        self.row = row
        self.col = col
        self.children = []


def build_tree(grid, th: P):

    def find_children(node, grid):
        row, col = node.row, node.col
        for r, c in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == node.value + 1:
                child = Node(grid[r][c], r, c)
                node.children.append(child)
                find_children(child, grid)

    x, y = p_to_xy(th)
    root = Node(0, y, x)

    if root:
        find_children(root, grid)

    return root


def visualize_tree(root):
    """
    Visualizes the tree using graphviz.
    """
    dot = Digraph(comment="Tree from Grid")

    def add_nodes_edges(node):
        """
        Recursively adds nodes and edges to the graph.
        """
        dot.node(str(id(node)), f"({node.row},{node.col}): {node.value}")
        for child in node.children:
            dot.edge(str(id(node)), str(id(child)))
            add_nodes_edges(child)

    add_nodes_edges(root)

    # Render the graph to a file (e.g., PDF, PNG)
    dot.format = "png"
    dot.render("tree_visualization", view=True)


def check_end_nodes(root):

    def is_end_node(node):
        return len(node.children) == 0

    def find_end_nodes(node):
        end_nodes = []
        if is_end_node(node):
            end_nodes.append(node)

        for child in node.children:
            end_nodes.extend(find_end_nodes(child))

        return end_nodes

    return find_end_nodes(root)


solution = 0

for th in trailheads:
    root = build_tree(grid, th)
    end_nodes = check_end_nodes(root)
    for node in end_nodes:
        if node.value == 9:
            solution += 1
    # visualize_tree(root)

print(solution)
