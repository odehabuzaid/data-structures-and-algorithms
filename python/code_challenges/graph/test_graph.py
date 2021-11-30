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


pytest.mark.skip("todo")


def test_get_nodes():

    graph = Graph()

    banana = graph.add_node("banana")

    apple = graph.add_node("apple")

    loner = Vertex("loner")

    expected = 2

    actual = len(graph.get_nodes())

    assert actual == expected


# pytest.mark.skip("pending")
# def test_get_neighbors():

#     graph = Graph()

#     banana = graph.add_node("banana")

#     apple = graph.add_node("apple")

#     graph.add_edge(apple, banana, 44)

#     neighbors = graph.get_neigbors(apple)

#     assert len(neighbors) == 1

#     neighbor_edge = neighbors[0]

#     assert neighbor_edge.vertex.value == "banana"

#     assert neighbor_edge.weight == 44


pytest.mark.skip("pending")
def test_bfs():
    graph = Graph()
    pandora = graph.add_node("Pandora")
    arendelle = graph.add_node("Arendelle")
    monstropolis = graph.add_node("Monstropolis")
    metroville = graph.add_node("Metroville")
    naboo = graph.add_node("Naboo")
    narnia = graph.add_node("Narnia")

    graph.add_edge(pandora, arendelle, 1)

    graph.add_edge(arendelle, metroville, 2)
    graph.add_edge(arendelle, monstropolis, 2)

    graph.add_edge(monstropolis, metroville, 2)
    graph.add_edge(monstropolis, naboo, 2)

    graph.add_edge(metroville, naboo, 2)
    graph.add_edge(metroville, narnia, 2)

    graph.add_edge(naboo, narnia, 2)

    # actual = graph.breadth_first_search(pandora, graph.return_nodes)

    # expected = ["Pandora", "Arendelle", "Metroville", "Monstropolis", "Naboo", "Narnia"]

    # for indx, v in enumerate(actual):
    #     print(expected[indx])
    #     assert v.__str__() == expected[indx]
