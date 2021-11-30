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
            # calculate the weight of each edge as cost
            for dest in destinations:
                if dest in neighbors:
                    cost += neighbors[dest].weight

                    # get the destination neighbor
                    neighbors_of = graph.get_neigbors(neighbors[dest].vertex)

                    # loop the  dest neighbor & check if any of destinations
                    # exists in the closet neighbor
                    # if exists
                    # add the weight of each edge to the cost
                    for next_neighborr in neighbors_of:
                        if next_neighborr in destinations:
                            cost += neighbors_of[next_neighborr].weight
            if cost:
                return "True, ${}".format(cost)

            return "False, $0"
