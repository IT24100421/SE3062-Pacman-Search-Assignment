# Student 3 Viva Code Trace

## Q3 — UCS Execution Flow

1. Get start state.
2. Push start node into util.PriorityQueue with cost 0.
3. bestCost stores the cheapest cost to each state.
4. Pop the node with minimum g(n).
5. Skip the node if it is an old expensive entry.
6. Check goal after popping.
7. Expand successors.
8. Calculate:
   newCost = cost + stepCost
9. If the new path is cheaper, update bestCost.
10. Push the successor with priority newCost.

### Important UCS Concepts

g(n):
Actual accumulated path cost from the start to node n.

Priority:
g(n)

Why goal-on-pop?
A goal can first be generated using an expensive path. UCS must wait
until the cheapest goal is removed from the priority queue.

Why bestCost?
The same state may be reached through multiple paths.

---

## Q6 — Corners Heuristic Execution Flow

State:
(position, visitedCorners)

1. Get current position.
2. Identify unvisited corners.
3. If none remain, return 0.
4. Generate every permutation of remaining corners.
5. For each order, calculate the Manhattan route:
   current position -> first corner -> next corner -> ...
6. Select the minimum route cost.
7. Return that value as h(n).

### Why admissible?

Manhattan distance ignores walls, so it cannot be greater than the
corresponding real maze distance.

Therefore the relaxed Manhattan tour cannot overestimate the true cost.

### Why consistent?

For one legal move:

h(n) <= 1 + h(n')

A single Pac-Man step changes Manhattan distance by at most one.

### Performance

Q6 result:
3/3

Path length:
106

Expanded nodes:
741

Assignment best threshold:
<= 1200