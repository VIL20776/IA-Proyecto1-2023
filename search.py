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

from inspect import _empty
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

    def expand(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (child,
        action, stepCost), where 'child' is a child to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that child.
        """
        util.raiseNotDefined()

    def getActions(self, state):
        """
          state: Search state

        For a given state, this should return a list of possible actions.
        """
        util.raiseNotDefined()

    def getActionCost(self, state, action, next_state):
        """
          state: Search state
          action: action taken at state.
          next_state: next Search state after taking action.

        For a given state, this should return the cost of the (s, a, s') transition.
        """
        util.raiseNotDefined()

    def getNextState(self, state, action):
        """
          state: Search state
          action: action taken at state

        For a given state, this should return the next state after taking action from state.
        """
        util.raiseNotDefined()

    def getCostOfActionSequence(self, actions):
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

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    """

    # Stack para almacenar los nodos que tenemos por explorar
    frontier = util.Stack()
    # Lista para almacenar los nodos que ya hemos explorado
    expanded = []
    # Añadimos el nodo inicial a la pila, con lista de acción vacía
    frontier.push((problem.getStartState(), []))

    # Mientras la pila frontier no esté vacía, seguimos explorando nodos
    while frontier.isEmpty() == False:
        # Sacamos el primer nodo de la pila y lo separamos en nodo y acciones
        current_state, current_moves = frontier.pop()
        # Si el nodo es el objetivo
        if problem.isGoalState(current_state):
            # Devolvemos la lista de acciones
            return current_moves
        # Si el nodo no ha sido explorado
        if current_state not in expanded:
            # Lo añadimos a la lista de nodos explorados
            expanded.append(current_state)
            # Exploramos los nodos hijos
            for child_state, child_move, child_cost in problem.expand(current_state):
                # Añadimos los movimientos que ya llevamos al hijo, más el nuevo movimiento que lleva al hijo
                new_moves = current_moves + [child_move]
                # Añadimos el hijo a la pila de nodos por explorar
                frontier.push((child_state, new_moves))
    # Si no hemos encontrado el nodo objetivo, regresamos una lista vacía
    return []

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""

    # Queue para almacenar los nodos que tenemos por explorar
    frontier = util.Queue()
    # Lista para almacenar los nodos que ya hemos explorado
    expanded = []
    # Añadimos el nodo inicial a la pila, con lista de acción vacía
    frontier.push((problem.getStartState(), []))
    # Lista para almacenar las rutas que vayan llegando a la meta
    routes = []

    # Mientras la pila frontier no esté vacía, seguimos explorando nodos
    while frontier.isEmpty() == False:
        # Sacamos el primer nodo de la pila y lo separamos en nodo y acciones
        current_state, current_moves = frontier.pop()
        # Si el nodo es el objetivo
        if problem.isGoalState(current_state):
            # Agregamos la ruta a la lista de rutas
            """ Usado en comparaciones de rutas """
            # routes.append((current_state, current_moves))

            # Devolvemos la lista de movimientos
            return current_moves
        # Si el nodo no ha sido explorado
        if current_state not in expanded:
            # Lo añadimos a la lista de nodos explorados
            expanded.append(current_state)
            # Exploramos los nodos hijos
            for child_state, child_move, child_cost in problem.expand(current_state):
                # Añadimos los movimientos que ya llevamos al hijo, más el nuevo movimiento que lleva al hijo
                new_moves = current_moves + [child_move]
                # Añadimos el hijo a la pila de nodos por explorar
                frontier.push((child_state, new_moves))

    """ Comparaciones de rutas para obtener ruta más corta """
    # # Agaramos el primer valor de la lista de rutas
    # best = routes[0][1];
    # # Comparamos las rutas para ver cuál es la mejor
    # for route in routes:
    #     # Si existe una ruta más corta que la que ya tenemos
    #     if len(route[1]) < len(best):
    #         # Reemplazamos la mejor ruta por la ruta más corta
    #         best = route[1]
    # # Devolvemos la mejor ruta
    # return best

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    # Queue para almacenar los nodos que tenemos por explorar
    frontier = util.PriorityQueue()
    # Lista para almacenar los nodos que ya hemos explorado
    expanded = []
    # Añadimos el nodo inicial a la pila, con lista de acción vacía
    frontier.push((problem.getStartState(), [], 0), 0)

    # Mientras la pila frontier no esté vacía, seguimos explorando nodos
    while frontier.isEmpty() == False:
        # Sacamos el primer nodo de la pila y lo separamos en nodo y acciones
        current_state, current_moves, g_score = frontier.pop()
        # Si el nodo es el objetivo
        if problem.isGoalState(current_state):
            # Agregamos la ruta a la lista de rutas
            return current_moves
        # Si el nodo no ha sido explorado
        if current_state not in expanded:
            # Lo añadimos a la lista de nodos explorados
            expanded.append(current_state)
            # Exploramos los nodos hijos
            for child_state, child_move, child_cost in problem.expand(current_state):
                # Añadimos los movimientos que ya llevamos al hijo, más el nuevo movimiento que lleva al hijo
                new_moves = current_moves + [child_move]
                new_g_score = g_score + child_cost
                new_f_score = new_g_score + heuristic(child_state, problem)
                # Añadimos el hijo a la pila de nodos por explorar
                frontier.update((child_state, new_moves, new_g_score), new_f_score)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
