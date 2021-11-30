from graph import Graph


def business_trip(graph, cities: list) -> str:
    destinations = cities[1:]
    position = cities[0]
    locations = graph.get_nodes()
    cost = 0

    # loop the nodes of the graph
    for location in locations:
        # check if  location equals the from position
        if location.value == position:
            # get neighbors of the starting position
            neighbors = graph.get_neigbors(location)

            # loop neighbors citires of starting position
            # check if any neighbor city is in destination
            # calculate the weight
            for dest in destinations:
                if dest in neighbors:
                    cost += neighbors[dest].weight
                    neighbors_of = graph.get_neigbors(neighbors[dest].vertex)

                    for nei_of in neighbors_of:
                        if nei_of in destinations:
                            cost += neighbors_of[nei_of].weight
            
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

    return graph


graph = create_graph()
print(business_trip(graph, ["Metroville", "Pandora"]))
print(business_trip(graph, ["Arendelle", "Monstropolis", "Naboo"]))
print(business_trip(graph, ["Narnia", "Arendelle", "Naboo"]))
print(business_trip(graph, ["Naboo", "Pandora"]))
