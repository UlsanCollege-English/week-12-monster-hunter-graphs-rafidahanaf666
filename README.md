# Week 12: Monster Hunter Graphs

## Student

Name: MD AHANAF AKIF RAFID

Student ID: 2412078

## Summary

This assignment builds graph structures to represent monster hunting routes between locations.

The locations represent places where monsters have been sighted.

The routes represent travel paths between locations.

The assignment also includes weighted routes, graph analysis functions, and a priority-based hunt system using a heap.

The hardest function was `build_weighted_hunter_map` because it needed to handle duplicate routes while keeping the lowest danger score.

## Approach

- `build_hunter_map`:
  - Created an undirected adjacency list.
  - Added both directions for every route.
  - Used sets to prevent duplicate neighbors.

- `build_weighted_hunter_map`:
  - Created an undirected weighted graph.
  - Checked that danger scores are positive.
  - Kept the lowest score when duplicate routes appeared.

- `map_summary`:
  - Counted the number of locations.
  - Counted routes by summing neighbor lists and dividing by two.

- `most_connected_location`:
  - Compared the number of neighbors for each location.
  - Returned the alphabetically first location in ties.

- `priority_hunt_order`:
  - Used Python's heapq module.
  - Removed items from the heap in priority order.

## Complexity

### `build_hunter_map`

- Time: O(E)
- Space: O(V + E)
- Why: Each route is processed once.

### `build_weighted_hunter_map`

- Time: O(E)
- Space: O(V + E)
- Why: Each weighted route is processed once.

### `map_summary`

- Time: O(V + E)
- Space: O(1)
- Why: Every adjacency list is visited once.

### `most_connected_location`

- Time: O(V)
- Space: O(1)
- Why: Every location is checked once.

### `priority_hunt_order`

- Time: O(N log N)
- Space: O(N)
- Why: Heap insertion and removal require log N time.

## Edge-Case Checklist

- [x] Empty graph
- [x] One route
- [x] Duplicate routes
- [x] Disconnected locations
- [x] Tie for most connected location
- [x] Positive weighted routes
- [x] Invalid zero or negative danger score
- [x] Empty priority report list

## Tests

Paste the result of your test run.

```bash
pytest -q
```

Result:

```text
13 passed
```

## Assistance & Sources

AI used? Yes

If yes, what did it help with?

- Understanding graph representations.
- Reviewing algorithm complexity.
- Generating test cases.

Other sources used:

- Python Documentation (heapq)
- Course notes