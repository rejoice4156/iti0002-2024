"""Find the shortest way back in a taxicab geometry."""


def shortest_way_back(path: str) -> str:
    """
    Find the shortest way back in a taxicab geometry.

    :param path: string of moves, where moves are encoded as follows:.
    N - north -  (1, 0)
    S - south -  (-1, 0)
    E - east  -  (0, 1)
    W - west  -  (0, -1)
    (first coordinate indicates steps towards north,
    second coordinate indicates steps towards east)

    :return: the shortest way back encoded the same way as :param path:.
    """
    path_back = ""
    d = {"N": (1, 0), "S": (-1, 0), "E": (0, 1), "W": (0, -1)}
    lat = 0
    long = 0
    for coord in path:
        lat += d[coord][0]
        long += d[coord][1]
    if lat > 0:
        while lat > 0:
            path_back += "S"
            lat -= 1
    elif lat < 0:
        while lat < 0:
            path_back += "N"
            lat += 1
    if long > 0:
        while long > 0:
            path_back += "W"
            long -= 1
    elif long < 0:
        while long < 0:
            path_back += "E"
            long += 1
    return path_back


if __name__ == '__main__':
    print(shortest_way_back("NNN"))  # "SSS"
    print(shortest_way_back("SS"))  # "NN"
    print(shortest_way_back("E"))  # "W"
    print(shortest_way_back("WWWW"))  # "EEEE"
    print(shortest_way_back(""))  # ""
    print(shortest_way_back("NESW"))  # ""
