# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
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
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first
    [2nd Edition: p 75, 3rd Edition: p 87]

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm
    [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    """
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())


    action_stack = recursiveDFS(problem, problem.getStartState())
    action_list = []
    if not action_stack:
        print "NO RESULT !!!!!!!!!!!!!"
        return action_list
    else:
        from util import Stack
        # Pop the stack and convert to an action list
        while not action_stack.isEmpty():
            action = action_stack.pop()
            action_list.append(action)
        return action_list

def recursiveDFS(problem, state=None, action=None, limit=900, visitedStateList=[]):
    """

    :param problem:
    :param state: Current position
    :param action: The action taken to move to current position
    :return: Action stack
    """
    from util import Stack
    # if the state is goal state, return this action
    if problem.isGoalState(state):
        action_stack = Stack()
        action_stack.push(action)
        return action_stack
    elif limit == 0:
        return False
    # else explore the next state
    successors = problem.getSuccessors(state)
    if successors is None:
        return False
    visitedStateList.append(state)
    for s in successors:
        # Avoid visiting visited states
        if is_visited(visitedStateList, s[0]):
            continue
        # Explore the next state
        action_stack = recursiveDFS(problem, s[0], s[1], limit-1, visitedStateList)
        # If this action leads to goal state
        if action_stack is not False:
            if action: # This checking is for initial calling of function recursiveDFS with action=None
                # Save the current action and then return
                action_stack.push(action)
            return action_stack
    # No next action available
    return False

def is_visited(visitedStateList, check_state):
    for s in visitedStateList:
        if s == check_state:
            return True
    return False

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    [2nd Edition: p 73, 3rd Edition: p 82]
    Test case: python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
    Test case: python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
    """
    from util import Queue
    import copy
    frontier = Queue()
    solution_space = Queue()
    explored = []

    if problem.isGoalState(problem.getStartState()):
        return []
    # Kick start with the start state
    frontier.push(problem.getStartState())
    # Save the action stack (ancestor path) together with the state
    solution_space.push([])
    explored.append(problem.getStartState())

    while True:
        if frontier.isEmpty():
            return False
        # Get the first one from the Queue to explore
        current_state = frontier.pop()
        action_stack = solution_space.pop()
        # Search for child states
        successors = problem.getSuccessors(current_state)
        for s in successors:
            (next_state, next_action, cost) = s
            # Skip visited state (frontier and explored), prevent infinite loop
            if is_visited(explored, next_state):
                continue
            # Deep copy the ancestor path and add this successor
            # so that we can return the action stack (ancestor path) whenever we found the goal state
            next_action_stack = copy.deepcopy(action_stack)
            next_action_stack.append(next_action)
            # Return action stack when found the goal state
            if problem.isGoalState(next_state):
                return next_action_stack
            # If not goal state, push the state into frontier for later exploration
            frontier.push(next_state)
            # Save the action stack (ancestor path) together with the state
            solution_space.push(next_action_stack)
            explored.append(next_state)

def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()
    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
