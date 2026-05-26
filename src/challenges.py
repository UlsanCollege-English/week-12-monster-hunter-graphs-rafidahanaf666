"""Week 12: Monster Hunter Graphs.

Complete each function using Python 3.11+.

Rules:
- Standard library only.
- Use type hints.
- Keep public function docstrings.
- Run tests with: pytest -q
"""

import heapq


def build_hunter_map(edges: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Build an undirected adjacency list from route pairs.

    Each tuple represents a two-way route between two monster sighting
    locations.
    """
    graph: dict[str, set[str]] = {}

    for start, end in edges:
        graph.setdefault(start, set()).add(end)
        graph.setdefault(end, set()).add(start)

    return {node: sorted(neighbors) for node, neighbors in graph.items()}


def build_weighted_hunter_map(
    edges: list[tuple[str, str, int]]
) -> dict[str, dict[str, int]]:
    """Build an undirected weighted graph from route triples."""
    graph: dict[str, dict[str, int]] = {}

    for start, end, weight in edges:
        if weight <= 0:
            raise ValueError("Danger score must be positive.")

        graph.setdefault(start, {})
        graph.setdefault(end, {})

        if end not in graph[start]:
            graph[start][end] = weight
            graph[end][start] = weight
        else:
            best = min(graph[start][end], weight)
            graph[start][end] = best
            graph[end][start] = best

    return graph


def map_summary(graph: dict[str, list[str]]) -> dict[str, int]:
    """Return the number of locations and undirected routes."""
    locations = len(graph)

    route_count = sum(len(neighbors) for neighbors in graph.values()) // 2

    return {
        "locations": locations,
        "routes": route_count,
    }


def most_connected_location(graph: dict[str, list[str]]) -> str | None:
    """Return the location with the most neighbors."""
    if not graph:
        return None

    return min(
        graph.keys(),
        key=lambda location: (-len(graph[location]), location),
    )


def priority_hunt_order(reports: list[tuple[int, str]]) -> list[str]:
    """Return monster sighting locations from most urgent to least urgent.

    Lower priority number means more urgent.
    """
    heap = []

    for priority, location in reports:
        heapq.heappush(heap, (priority, location))

    result = []

    while heap:
        _, location = heapq.heappop(heap)
        result.append(location)

    return result