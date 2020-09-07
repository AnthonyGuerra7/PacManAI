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


#Anthony Lopez-Guerra
#010561185

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

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    #print "Start:", problem.getStartState()
    #print "Is the start goal?", problem.isGoalState(problem.getStartState())
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())
    from util import Stack
    
    #This is a stack which contain the position that the pacman will travel
    PositionStack = Stack()
    #This will contain all of the visited states
    Visited = []  
    #This will contain the path from the starting state
    Path = []
    #Test to see if the inital state is the goal state which you are intending to find.
    if problem.isGoalState(problem.getStartState()):
        return []
    #This will start to push onto the stack from the beginning and will find a solution. The initial path is an empty list
    PositionStack.push((problem.getStartState(),[]))

    while(True):

        #This will end the program is a solution cannot be found
        if PositionStack.isEmpty():
            return []

        #This will gather the information of the current state (p1,p2) and save it to the 
        #variable p1p2 and Path
        p1p2,Path = PositionStack.pop()
        Visited.append(p1p2)

        #Check to see if new position p1p2 is the end goal
        if problem.isGoalState(p1p2):
            return Path

        #Get Possible Successors of the current state
        q1q2 = problem.getSuccessors(p1p2)

        #This will add new states in the stack based on the successors
        if q1q2:
            for option in q1q2:
                if option[0] not in Visited:

                    #Calculate a new path
                    NPath = Path + [option[1]]
                    PositionStack.push((option[0],NPath))
                    

    #util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from util import Queue
    #This is a queue which contain the position that the pacman will travel
    PositionQueue = Queue()
    #This will contain all of the visited states
    Visited = []  
    #This will contain the path from the starting state
    Path = []
    #Test to see if the inital state is the goal state which you are intending to find.
    if problem.isGoalState(problem.getStartState()):
        return []

    #This will start to push onto the queue from the beginning and will find a solution. The initial path is an empty list
    PositionQueue.push((problem.getStartState(),[]))

    while(True):

        #This will end the program is a solution cannot be found
        if PositionQueue.isEmpty():
            return []

        #This will gather the information of the current state (p1,p2)
        p1p2,Path = PositionQueue.pop()
        Visited.append(p1p2)

        #Check to see if new position p1p2 is the end goal
        if problem.isGoalState(p1p2):
            return Path

        #Get Possible Successors of the current state
        q1q2 = problem.getSuccessors(p1p2)

        #This will add new states in the queue
        if q1q2:
            for option in q1q2:
                if option[0] not in Visited and option[0] not in (state[0] for state in PositionQueue.list):

                    #Calculate a new path
                    NPath = Path + [option[1]]
                    PositionQueue.push((option[0],NPath))

    
    #util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    from util import PriorityQueue

    #This is a priority queue which contain the position that the pacman will travel
    Posqueue = PriorityQueue()

    #This will contain all of the visited states
    visited = [] 

    #This will contain the path from the starting state
    path = [] 

    #Test to see if the inital state is the goal state which you are intending to find.
    if problem.isGoalState(problem.getStartState()):
        return []

    #This will start to push onto the queue from the beginning and will find a solution. The initial path is an empty list
    Posqueue.push((problem.getStartState(),[]),0)

    while(True):

        #This will end the program is a solution cannot be found
        if Posqueue.isEmpty():
            return []

        #This will gather the information of the current state (p1,p2)
        p1p2,path = Posqueue.pop() 
        visited.append(p1p2)

        #Check to see if new position p1p2 is the end goal
        if problem.isGoalState(p1p2):
            return path

        #Get Possible Successors of the current state
        q1q2 = problem.getSuccessors(p1p2)

        # This will add new states to the queue
        if q1q2:
            for option in q1q2:
                if option[0] not in visited and (option[0] not in (state[2][0] for state in Posqueue.heap)):

                    
                    #Calculate a new path
                    NPath = path + [option[1]]
                    p = problem.getCostOfActions(NPath)
                    Posqueue.push((option[0],NPath),p)

                 #Compares if the current path is cheaper from the previous option
                elif option[0] not in visited and (option[0] in (state[2][0] for state in Posqueue.heap)):
                    for state in Posqueue.heap:
                        if state[2][0] == option[0]:
                            op = problem.getCostOfActions(state[2][1])

                    np = problem.getCostOfActions(path + [option[1]])

                    if op > np:
                        NPath = path + [option[1]]
                        Posqueue.update((option[0],NPath),np)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

from util import PriorityQueue
class MyPQ(PriorityQueue):
    def __init__(self,problem, priorityF):
        self.priorityF = priorityF
        PriorityQueue.__init__(self)
        self.problem = problem

    def push(self,option, heuristic):
        PriorityQueue.push(self,option, self.priorityF(self.problem,option,heuristic))


#This will be used to calculate your f = g + h
def f(problem,state,heuristic):
    return problem.getCostOfActions(state[1]) + heuristic(state[0], problem)


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    #This is a queue which contain the position that the pacman will travel
    PositionQueue = MyPQ(problem,f)
    
    #This will contain all of the visited states
    Visited = []  

    #This will contain the path from the starting state
    Path = []

    #Test to see if the inital state is the goal state which you are intending to find.
    if problem.isGoalState(problem.getStartState()):
        return []

    #This will start to push onto the queue from the beginning and will find a solution. The initial path is an empty list
    elem = (problem.getStartState(),[])
    PositionQueue.push(elem,heuristic)

    while(True):

        #This will end the program is a solution cannot be found
        if PositionQueue.isEmpty():
            return []

        #This will gather the information of the current state (p1,p2)
        p1p2,Path = PositionQueue.pop()

        #if a path with lower cost has been previously found. Skip
        if p1p2 in Visited:
            continue

        Visited.append(p1p2)

        #Check to see if new position p1p2 is the end goal
        if problem.isGoalState(p1p2):
            return Path

        #Get Possible Successors of the current state
        q1q2 = problem.getSuccessors(p1p2)

        #This will add new states in the stack 
        if q1q2:
            for option in q1q2:
                if option[0] not in Visited:

                    #Calculate a new path
                    NPath = Path + [option[1]]
                    elem = (option[0], NPath)
                    PositionQueue.push(elem, heuristic)

    #util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
