# Student 3 — Q3 Uniform Cost Search

## Responsibility

Student 3 implemented:

- Q3 Uniform Cost Search
- Function: `uniformCostSearch(problem)`
- File: `search.py`

## Algorithm Idea

Uniform Cost Search expands the frontier node with the lowest total accumulated path cost. The value `g(n)` represents the actual cost from the start state to the current state. The implementation uses `util.PriorityQueue`, with `g(n)` as the priority rather than the number of actions taken.

## Frontier Node Structure

Each frontier node has the form `(state, actions, accumulatedCost)`:

- `state` is the current search state.
- `actions` is the path of actions used to reach that state.
- `accumulatedCost` is the total cost from the start state.

## `bestCost`

The `bestCost` dictionary records the cheapest discovered path cost for each state. This is necessary because the same state may be discovered through multiple paths, and a later path may have a lower cost.

## Cheaper-Path Relaxation

The implementation accepts a successor when `successor not in bestCost or newCost < bestCost[successor]`. It then:

- Updates `bestCost`.
- Stores the new action path.
- Pushes the successor into the priority queue with `newCost` as its priority.

## Stale Frontier Entries

An older, more expensive entry can remain in the priority queue after a cheaper route to the same state is discovered. The implementation skips an outdated entry when its stored cost no longer matches `bestCost[state]`.

## Goal Test

UCS tests whether a state is a goal when the cheapest valid node is popped from the priority queue. A goal may first be discovered through an expensive route while a cheaper route is still waiting to be explored, so the algorithm does not return a goal as soon as it is generated.

## Optimality

UCS finds a least-cost solution when step costs are non-negative.

## Testing

Command: `py -3.11 autograder.py -q q3`

Manual PowerShell result:

```text
Question q3: 3/3
Total: 3/3
```

Q3 passed all supplied autograder tests.

## Report Evidence Reminder

Student 3 report evidence should include:

- Q3 autograder screenshot
- Q3 code screenshot
- Git commit history
- Student 3 branch / pull request evidence

# Student 3 — Q6 Corners Heuristic

## Responsibility

Student 3 implemented `cornersHeuristic(state, problem)` in `searchAgents.py`.

## Q5 State Used

The heuristic uses the confirmed Q5 state:

`(position, visitedCorners)`

- `position` is the current Pac-Man coordinate.
- `visitedCorners` is a `frozenset` of visited corner coordinates.

The heuristic reads this state without modifying it. The Q5 dependency passed its supplied autograder tests with `Question q5: 3/3`.

## Heuristic Design

The heuristic:

1. Finds all remaining unvisited corners.
2. Generates every possible order for visiting them.
3. Calculates the Manhattan route cost for each order, starting at Pac-Man's current position.
4. Returns the minimum route cost.

There are at most four corners, so at most `4! = 24` visit orders are checked.

## Why Manhattan Distance

Manhattan distance ignores maze walls, so `Manhattan distance <= actual maze path distance`. This makes it a computationally inexpensive lower-bound component.

## Admissibility

The heuristic solves a relaxed version of the CornersProblem because it ignores walls. Every Manhattan route through the remaining corners costs no more than its corresponding real maze route. Taking the minimum relaxed route therefore cannot overestimate the true remaining cost, so the heuristic is admissible.

## Consistency

Consistency requires `h(n) <= c(n,n') + h(n')`. Each legal Pac-Man move costs `1`, and moving one square changes Manhattan distance by at most `1`. Because the heuristic is the optimal remaining cost in the relaxed Manhattan problem, one real move cannot reduce that relaxed cost by more than the move cost. Therefore the heuristic is consistent.

## Goal State

When all corners have been visited, `h(goal) = 0`.

## Final Testing

Command: `py -3.11 autograder.py -q q6`

Dependency tests:

```text
Question q4: 3/3
```

Q6:

```text
Question q6: 3/3
```

Total shown:

```text
6/6
```

- Path length: `106`
- Nodes expanded: `741`

## Performance

The assignment's full-efficiency threshold is `<= 1200` expanded nodes. The actual result was `741` expanded nodes, so the heuristic satisfies the highest Q6 node-efficiency level.

## Viva Summary

1. **What does the heuristic estimate?** The relaxed remaining cost to visit every unvisited corner.
2. **Why use permutations?** The best visit order depends on Pac-Man's current position and which corners remain.
3. **Why is checking every order practical?** There are at most four corners, so at most 24 permutations.
4. **Why not use `mazeDistance` for every heuristic call?** Manhattan distance is much cheaper to compute and still provides an admissible lower bound.
5. **What does admissible mean?** The heuristic never overestimates the true remaining cost.
6. **What does consistent mean?** `h(n) <= c(n,n') + h(n')` for every transition.
