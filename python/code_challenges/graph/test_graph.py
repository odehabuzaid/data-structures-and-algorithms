import pytest
from graph import Graph, Vertex


@pytest.fixture()
def create_graph():
    graph = Graph()
    pandora = graph.add_node("Pandora")
    arendelle = graph.add_node("Arendelle")
    monstropolis = graph.add_node("Monstropolis")
    metroville = graph.add_node("Metroville")
    naboo = graph.add_node("Naboo")
    narnia = graph.add_node("Narnia")

    graph.add_edge(pandora, arendelle, 150)
    graph.add_edge(pandora, metroville, 82)

    graph.add_edge(arendelle, pandora, 150)
    graph.add_edge(arendelle, monstropolis, 42)
    graph.add_edge(arendelle, metroville, 99)

    graph.add_edge(metroville, pandora, 82)
    graph.add_edge(metroville, arendelle, 99)
    graph.add_edge(metroville, naboo, 26)
    graph.add_edge(metroville, monstropolis, 105)
    graph.add_edge(metroville, narnia, 37)

    graph.add_edge(monstropolis, arendelle, 42)
    graph.add_edge(monstropolis, metroville, 105)
    graph.add_edge(monstropolis, naboo, 73)

    graph.add_edge(naboo, metroville, 26)
    graph.add_edge(naboo, narnia, 250)

    graph.add_edge(narnia, metroville, 37)
    graph.add_edge(naboo, naboo, 250)
    return graph


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

    neighbors = graph.get_neigbors("apple")

    assert len(neighbors) == 1
    assert neighbors.__str__() == "{'banana': banana}"


def test_bfs(create_graph):
    graph = create_graph
    nodes = graph.get_nodes()

    for location in nodes:
        if location.value == "Pandora":
            actual = graph.breadth_first_search(location, graph.return_nodes)

    expected = ["Pandora", "Arendelle", "Metroville", "Monstropolis", "Naboo", "Narnia"]

    for indx, v in enumerate(actual):
        print(expected[indx])
        assert v.__str__() == expected[indx]


from b_trip import business_trip


def test_graph_business_trip_two_citis_connected(create_graph):
    graph = create_graph

    expected = "True, $82"

    actual = business_trip(graph, ["Metroville", "Pandora"])

    assert actual == expected


def test_graph_business_trip_two_citis_not_connected(create_graph):
    graph = create_graph

    expected = "False, $0"

    actual = business_trip(graph, ["Naboo", "Pandora"])

    assert actual == expected

    actual = business_trip(graph, ["Narnia", "Arendelle", "Naboo"])

    assert actual == "False, $0"


def test_graph_business_trip_three_cities(create_graph):
    graph = create_graph

    expected = "True, $115"

    actual = business_trip(graph, ["Arendelle", "Monstropolis", "Naboo"])

    assert actual == expected
