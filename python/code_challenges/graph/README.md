# Graphs
A graph is a non-linear data structure that can be looked at as a collection of vertices `nodes` potentially connected by line segments named edges.


-   _Vertex_ - A vertex, also called a “node”, is a data object that can have zero or more adjacent vertices.
-   _Edge_ - An edge is a connection between two nodes.
-   _Neighbor_ - The neighbors of a node are its adjacent nodes, i.e., are connected via an edge.
-   _Degree_ - The degree of a vertex is the number of edges connected to that vertex.


## Challenge
Implement a Graph. The graph should be represented as an adjacency list.


## Approach & Efficiency
Time --> O(n)

Space --> O(n)

## API
- add node

    Add a node to the graph
    - Arguments: value
    - Returns: The added node

- add edge

    Adds a new edge between two nodes in the graph-
    If specified, assign a weight to the edge
    Both nodes should already be in the Graph
    - Arguments: 2 nodes to be connected by the edge, weight (optional)
    - Returns: nothing
- get nodes

    - Arguments: none
    - Returns all of the nodes in the graph as a collection (set, list, or similar)


- get neighbors

    Include the weight of the connection in the returned collection
    - Arguments: node
    - Returns a collection of edges connected to the given node

- size
    - Arguments: none
    - Returns the total number of nodes in the graph
