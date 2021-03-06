class Queue:
    def __init__(self):
        self.dq = []

    def enqueue(self, value):
        self.dq.append(value)

    def dequeue(self):
        return self.dq.pop(0)

    def __len__(self):
        return len(self.dq)


class Stack:
    def __init__(self):
        """
        The constructor method for the stack class and it initializes the dq property to a new double ended queue instance.
        """
        self.dq = []

    def push(self, value):
        """
        Store the passed value in a node and then push the node on top of the stack.

        PARAMETERS
        ----------
                value: any
                        The value that will get stored in a node to be pushed on top of the stack.
        """
        self.dq.append(value)

    def pop(self):
        """
        Return the top node in a stack.
        """
        self.dq.pop()


class Vertex:
    """
    Class for Adding a node to the graph
    Arguments: value
    Returns: The added node
    """

    def __init__(self, value):
        """
        Initalization for a Vertex to hold a value.

        """
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)


class Edge:
    """
    a class for Adding a new edge between two nodes in the graph
    If specified, assigning a weight to the edge
    Arguments: 2 nodes to be connected by the edge, weight (optional)
    Returns: nothing

    """

    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight

    def __str__(self):
        return str(self.vertex)

    def __repr__(self):
        return str(self.vertex)


class Graph:
    def __init__(self):
        """
        Initalization for a hashmap to hold the vertices
        """
        self.__adjacency_list = {}
        self.dfs_visited = set()

    def add_node(self, value):
        """
        Method for Adding a node to the graph
        Arguments: value
        Returns: The added node
        """
        # new node
        v = Vertex(value)
        self.__adjacency_list[v] = []
        return v

    def add_edge(self, start_vertex, end_vertex, weight=0):
        """Adds an edge to the graph"""
        if start_vertex not in self.__adjacency_list:
            raise KeyError("Start Vertex not found in graph")

        if end_vertex not in self.__adjacency_list:
            raise KeyError("End Vertex not found in graph")
        edge = Edge(end_vertex, weight)
        self.__adjacency_list[start_vertex].append(edge)

    def size(self):
        return len(self.__adjacency_list)

    def get_nodes(self):
        """
        Method to get all nodes in Graph
        Arguments: None
        return: All nodes
        """
        return self.__adjacency_list

    def get_neigbors(self, vertex):
        """ """
        neigbors = None

        for node in self.get_nodes():

            if node.value == vertex:
                neigbors = self.__adjacency_list.get(node, [])

        neigbors_dict = {}
        if neigbors:
            for neigbor in neigbors:
                neigbors_dict[neigbor.__str__()] = neigbor

        return neigbors_dict

    def return_nodes(self, data):
        return data

    def breadth_first_search(self, start_vertex, action=(lambda _: None)):
        queue = Queue()
        visited = set()
        nodes = list()

        queue.enqueue(start_vertex)

        while len(queue):
            current_vertex = queue.dequeue()
            visited.add(current_vertex)
            nodes.append(current_vertex)

            neighbors = self.get_neigbors(current_vertex)

            for edge in neighbors:

                neighbor = neighbors[edge].vertex
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.enqueue(neighbor)

        return action(nodes)

    def depth_first_search(self, start_vertex):
        self.dfs_visited.add(start_vertex)

        for neighbour in self.get_neigbors(start_vertex):
            if neighbour not in self.dfs_visited:
                self.depth_first_search(neighbour)
        return self.dfs_visited
