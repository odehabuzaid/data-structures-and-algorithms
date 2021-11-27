import pytest
from graph import Graph, Vertex


def test_add_node():
    graph = Graph()
    expected = "test"
    actual = graph.add_node("test").value
    assert actual == expected


def test_size_empty():

    graph = Graph()

    expected = 0

    actual = graph.size()

    assert actual == expected


def test_size():

    graph = Graph()

    graph.add_node("spam")

    expected = 1

    actual = graph.size()

    assert actual == expected


def test_add_edge_interloper_start():

    graph = Graph()

    start = Vertex("start")

    end = graph.add_node("end")

    with pytest.raises(KeyError):
        graph.add_edge(start, end)


def test_add_edge_interloper_end():

    graph = Graph()

    end = Vertex("end")

    start = graph.add_node("start")

    with pytest.raises(KeyError):
        graph.add_edge(start, end)


def test_get_nodes():

    graph = Graph()

    banana = graph.add_node("banana")

    apple = graph.add_node("apple")

    loner = Vertex("loner")

    expected = 2

    actual = len(graph.get_nodes())

    assert actual == expected


def test_get_neighbors():

    graph = Graph()

    banana = graph.add_node("banana")

    apple = graph.add_node("apple")

    graph.add_edge(apple, banana, 44)

    neighbors = graph.get_neigbors(apple)

    assert len(neighbors) == 1

    neighbor_edge = neighbors[0]

    assert neighbor_edge.vertex.value == "banana"

    assert neighbor_edge.weight == 44


def test_bfs():

    graph = Graph()

    banana = graph.add_node("banana")

    apple = graph.add_node("apple")

    tst = graph.add_node("test")
    graph.add_edge(apple, banana, 44)
    graph.add_edge(apple, tst, 45)

    graph.add_edge(tst, banana, 45)

    neighbors = list(graph.breadth_first_search(apple, graph.get_neigbors))

    expected = ["banana", "test", "banana"]

    for indx, v in enumerate(neighbors):
        assert v.__str__() == expected[indx]
