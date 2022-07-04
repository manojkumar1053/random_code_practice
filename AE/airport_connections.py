
def airportConnections(airports, routes, startingAirport):
    # Write your code here.
    airport_graph = create_airport_graph(airports, routes)
    #unreacahable_airport_nodes = get_unreacahable_airport_nodes(airport_graph, airports, startingAirport)



def create_airport_graph(airports, routes):
    airport_graph = {}
    for airport in airports:
        airport_graph[airport] = AirportNode(airport)
    for route in routes:
        airport, connection = route
        airport_graph[airport].connections.append(connection)
    return airport_graph


class AirportNode:
    def __init__(self, airport) -> None:
        self.airport = airport
        self.connections = []
        self.is_raechable = True
        self.unreachable_connections = []

routes = [
            ["DSM", "ORD"],
            ["ORD", "BGI"],
            ["BGI", "LGA"],
            ["SIN", "CDG"],
            ["CDG", "SIN"],
            ["CDG", "BUD"],
            ["DEL", "DOH"],
            ["DEL", "CDG"],
            ["TLV", "DEL"],
            ["EWR", "HND"],
            ["HND", "ICN"],
            ["HND", "JFK"],
            ["ICN", "JFK"],
            ["JFK", "LGA"],
            ["EYW", "LHR"],
            ["LHR", "SFO"],
            ["SFO", "SAN"],
            ["SFO", "DSM"],
            ["SAN", "EYW"],
        ]

AIRPORTS = [
    "BGI",
    "CDG",
    "DEL",
    "DOH",
    "DSM",
    "EWR",
    "EYW",
    "HND",
    "ICN",
    "JFK",
    "LGA",
    "LHR",
    "ORD",
    "SAN",
    "SFO",
    "SIN",
    "TLV",
    "BUD",
]


STARTING_AIRPORT = "LGA"

print(create_airport_graph(airports=AIRPORTS, routes=routes))