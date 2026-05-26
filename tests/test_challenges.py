from src.challenges import (
    build_hunter_map,
    build_weighted_hunter_map,
    map_summary,
    most_connected_location,
    priority_hunt_order,
)

import pytest


def test_build_hunter_map_basic() -> None:
    graph = build_hunter_map(
        [
            ("A", "B"),
            ("A", "C"),
        ]
    )

    assert graph["A"] == ["B", "C"]
    assert graph["B"] == ["A"]
    assert graph["C"] == ["A"]


def test_build_hunter_map_duplicate_routes() -> None:
    graph = build_hunter_map(
        [
            ("A", "B"),
            ("A", "B"),
            ("B", "A"),
        ]
    )

    assert graph["A"] == ["B"]
    assert graph["B"] == ["A"]


def test_build_hunter_map_empty() -> None:
    assert build_hunter_map([]) == {}


def test_build_weighted_hunter_map_basic() -> None:
    graph = build_weighted_hunter_map(
        [
            ("A", "B", 4),
            ("B", "C", 2),
        ]
    )

    assert graph["A"]["B"] == 4
    assert graph["B"]["A"] == 4
    assert graph["B"]["C"] == 2
    assert graph["C"]["B"] == 2


def test_build_weighted_hunter_map_duplicate_keep_lowest() -> None:
    graph = build_weighted_hunter_map(
        [
            ("A", "B", 10),
            ("A", "B", 3),
            ("A", "B", 7),
        ]
    )

    assert graph["A"]["B"] == 3
    assert graph["B"]["A"] == 3


def test_build_weighted_hunter_map_invalid_weight() -> None:
    with pytest.raises(ValueError):
        build_weighted_hunter_map(
            [
                ("A", "B", 0),
            ]
        )


def test_map_summary() -> None:
    graph = {
        "A": ["B", "C"],
        "B": ["A"],
        "C": ["A"],
    }

    assert map_summary(graph) == {
        "locations": 3,
        "routes": 2,
    }


def test_map_summary_empty() -> None:
    assert map_summary({}) == {
        "locations": 0,
        "routes": 0,
    }


def test_most_connected_location() -> None:
    graph = {
        "A": ["B", "C"],
        "B": ["A"],
        "C": ["A"],
    }

    assert most_connected_location(graph) == "A"


def test_most_connected_location_tie() -> None:
    graph = {
        "A": ["B"],
        "B": ["A"],
    }

    assert most_connected_location(graph) == "A"


def test_most_connected_location_empty() -> None:
    assert most_connected_location({}) is None


def test_priority_hunt_order() -> None:
    reports = [
        (3, "Park"),
        (1, "Mall"),
        (2, "Station"),
    ]

    assert priority_hunt_order(reports) == [
        "Mall",
        "Station",
        "Park",
    ]


def test_priority_hunt_order_empty() -> None:
    assert priority_hunt_order([]) == []