# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    fringe = util.Stack()
    visited = set()

    startState = problem.getStartState()
    fringe.push((startState, []))

    while not fringe.isEmpty():
        state, actions = fringe.pop()

        if problem.isGoalState(state):
            return actions

        if state not in visited:
            visited.add(state)

            for successor, action, stepCost in problem.getSuccessors(state):
                if successor not in visited:
                    fringe.push((successor, actions + [action]))

    return []

def breadthFirstSearch(problem: SearchProblem):
    """
    Search the shallowest nodes in the search tree first.
    BFS explores the state space level-by-level using a FIFO (First-In, First-Out) queue.
    This guarantees finding the shortest path when all step costs are equal (cost = 1).
    """
    # 1. Initialize the FIFO Queue frontier and visited set for graph search
    fringe = util.Queue()
    visited = set()

    # 2. Push the starting state and an empty list of actions onto the queue
    startState = problem.getStartState()
    fringe.push((startState, []))

    # 3. Process states until the queue is empty
    while not fringe.isEmpty():
        # Pop the shallowest unvisited state (FIFO ordering)
        state, actions = fringe.pop()

        # Goal check: verify if the current state reaches the goal
        if problem.isGoalState(state):
            return actions

        # Graph search: only expand states that haven't been visited yet
        if state not in visited:
            visited.add(state)

            # 4. Explore all legal successors and enqueue them with accumulated actions
            for successor, action, stepCost in problem.getSuccessors(state):
                if successor not in visited:
                    fringe.push((successor, actions + [action]))

    # Return an empty path if no solution was found
    return []

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    fringe = util.PriorityQueue()
    startState = problem.getStartState()

    startActions = []
    startCost = 0
    startNode = (startState, startActions, startCost)

    # Order frontier nodes by their accumulated path cost g(n).
    fringe.push(startNode, startCost)
    # Store the cheapest discovered cost for each state.
    bestCost = {startState: startCost}

    while not fringe.isEmpty():
        state, actions, cost = fringe.pop()

        # Skip stale entries when a cheaper route is already known.
        if cost != bestCost.get(state):
            continue

        # Test the goal only after popping the cheapest valid node.
        if problem.isGoalState(state):
            return actions

        for successor, action, stepCost in problem.getSuccessors(state):
            newCost = cost + stepCost
            newActions = actions + [action]

            # Relax the successor when this path is cheaper.
            if successor not in bestCost or newCost < bestCost[successor]:
                bestCost[successor] = newCost
                successorNode = (successor, newActions, newCost)
                fringe.push(successorNode, newCost)

    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    fringe = util.PriorityQueue()
    startState = problem.getStartState()
    bestCost = {startState: 0}
    fringe.push((startState, [], 0), heuristic(startState, problem))

    while not fringe.isEmpty():
        state, actions, cost = fringe.pop()

        # A cheaper route may have been queued since this entry was added.
        if cost > bestCost[state]:
            continue

        if problem.isGoalState(state):
            return actions

        for successor, action, stepCost in problem.getSuccessors(state):
            nextCost = cost + stepCost
            if successor not in bestCost or nextCost < bestCost[successor]:
                bestCost[successor] = nextCost
                priority = nextCost + heuristic(successor, problem)
                fringe.push((successor, actions + [action], nextCost), priority)

    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
