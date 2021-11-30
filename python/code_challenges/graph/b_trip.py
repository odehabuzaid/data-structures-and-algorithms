from graph import Graph


def business_trip(graph, cities: list) -> int or None:
    destinations = cities[1:]  #
    position = cities[0]
    locations = graph.get_nodes()
    cost = 0

    for location in locations:
        if location.value == position:
            neighbors = graph.get_neigbors(location)

            print(destinations)
            for dest in destinations:
                if dest in neighbors.__repr__():
                    print(dest)
                    cost += neighbors[dest].weight

                else:
                    neighbors_of = graph.get_neigbors(neighbors[dest].vertex)
                    if dest in neighbors_of.__repr__():
                        print(dest)
                        cost += neighbors[dest].weight


            if cost:
                return "True, ${}".format(cost)

            return "False, $0"


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

    nodes = graph.get_nodes()
    print(type(nodes))

    # for i in nodes:
    #     if i.value == "Metroville":
    #         print(i.value)

    print("=" * 30)
    return graph


graph = create_graph()

print(business_trip(graph, ["Arendelle", "Monstropolis", "Naboo"]))
