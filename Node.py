import Action
import State


class Node:
    """
    Esta clase representa un nodo en un árbol de búsqueda.
    Cada nodo tiene un estado, una acción que llevó a ese estado, una lista de acciones posibles, un nodo father,
    una lista de nodos hijos, un precio, y diccionarios para heurísticas y values.
    """
    def __init__(
            self,
            state: State,
            action: Action = None,
            actions: list[Action] = [],
            father: 'Node' = None
    ):
        self.state = state  # El estado del nodo
        self.action = action  # La acción que llevó a este estado
        self.actions = actions  # Las acciones posibles desde este estado
        self.father = father  # El nodo father
        self.children = []  # Los nodos hijos
        self.price = 0  # El precio para llegar a este nodo
        self.heuristics = {}  # Las heurísticas calculadas para este nodo
        self.values = {}  # Los valores calculados para este nodo

    def __str__(self):
        return self.state.name

    def expandir(self, problem):
        self.children = []
        if not self.actions:
            if self.state.name not in problem.actions.keys():
                return self.children
            self.actions = problem.actions[self.state.name]
        for action in self.actions.keys():
            action_child = action(action)
            nuevo_state = problem.result(self.state, action_child)
            actions_nuevo = {}
            if nuevo_state.name in problem.actions.keys():
                actions_nuevo = problem.actions[nuevo_state.name]
            child = Node(nuevo_state, action_child, actions_nuevo, self)
            price = self.father.price if self.father else 0
            price += problem.price_action(self.state, action_child)
            child.price = price
            child.heuristics = problem.heuristics[child.state.name]
            child.values = {state: heuristica + child.price
                             for state, heuristica
                             in child.heuristics.items()}
            self.children.append(child)
        return self.children

    def best_child(self, problem, metrica='valor', criterio='menor'):
        if not self.children:
            return None
        mejor = self.children[0]
        for child in self.children:
            for objetivo in problem.state_objetivo:
                if metrica == 'valor':
                    valor_child = child.values[objetivo.name]
                    valor_mejor = mejor.values[objetivo.name]
                    if (criterio == 'menor' and valor_child < valor_mejor):
                        mejor = child
                    elif (criterio == 'mayor' and valor_child > valor_mejor):
                        mejor = child
                elif metrica == 'heuristica':
                    heuristica_child = child.heuristics[objetivo.name]
                    heuristica_mejor = mejor.heuristics[objetivo.name]
                    if (criterio == 'menor' and heuristica_child < heuristica_mejor):
                        mejor = child
                    elif (criterio == 'mayor' and heuristica_child > heuristica_mejor):
                        mejor = child
                elif metrica == 'price':
                    price_camino_child = problem.price_camino(child)
                    price_camino_mejor = problem.price_camino(mejor)
                    if (criterio == 'menor' and price_camino_child < price_camino_mejor):
                        mejor = child
                    elif (criterio == 'mayor' and price_camino_child > price_camino_mejor):
                        mejor = child
        return mejor
