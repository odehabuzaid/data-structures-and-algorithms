def business_trip(graph, cities: list) -> str:
    def check_out(cost):
        if cost:
            return "True, ${}".format(cost)
        return "False, $0"

    destinations = cities[1:]
    position = cities[0]
    cost = 0
    # get neighbors of the starting position
    neighbors = graph.get_neigbors(position)

    # loop neighbors cities of starting position
    # check if any neighbor city is in destination
    # calculate the weight of each edge as cost
    for dest in destinations:
        if dest in neighbors:
            cost += neighbors[dest].weight

            # get the destination neighbor
            next_destination = neighbors[dest].vertex.value
            neighbors_of = graph.get_neigbors(next_destination)

            # loop the  dest neighbors & check if any of destinations
            # exists in the closet neighbor
            # if exists
            # add the weight of each edge to the cost
            for next_neighborr in neighbors_of:
                if next_neighborr in destinations:
                    cost += neighbors_of[next_neighborr].weight
        else:
            return check_out(cost)
    return check_out(cost)
