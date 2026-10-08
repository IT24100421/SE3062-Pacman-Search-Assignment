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

## Q5 Dependency / State Contract

The current `CornersProblem` implementation uses the state:

`(position, visitedCorners)`

- `position` is the current Pac-Man coordinate as an `(x, y)` tuple.
- `visitedCorners` is a `frozenset` containing the corner-coordinate tuples already visited.

`getStartState()` creates this format and includes the starting position when it is a corner. `getSuccessors()` reads the same format and creates a new `frozenset` containing the next position when Pac-Man moves onto a corner. `isGoalState()` treats the state as complete when the number of visited corners equals the number of problem corners. Both components are hashable, so the complete state is hashable.

`cornersHeuristic()` must read this exact representation without modifying the state.

Q5 validation status: Automated IDE validation was unavailable because Python 3.11 is not installed in the IDE environment. Static inspection confirmed that the Q5 state representation is consistent and that the historical `frozenset`/Boolean-list mismatch is not present. Manual PowerShell validation with `py -3.11 autograder.py -q q5` remains pending.
