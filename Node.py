import Action
import State


class Node:
    def __init__(
            self,
            state: State,
            action: Action = None,
            actions: list[Action] = None,
            father: 'Node' = None
    ):
        self.state = state
        self.action = action
        self.actions = actions
        self.padre = father
        self.children = []
        self.costo = 0
        self.heuristicas = {}
        self.valores = {}

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
            costo = self.padre.costo if self.padre else 0
            costo += problem.costo_action(self.state, action_child)
            child.costo = costo
            child.heuristicas = problem.heuristicas[child.state.name]
            child.valores = {state: heuristica + child.coste
                             for state, heuristica
                             in child.heuristicas.items()}
            self.children.append(child)
        return self.children

    def child_mejor(self, problem, metrica='valor', criterio='menor'):
        if not self.children:
            return None
        mejor = self.children[0]
        for child in self.children:
            for objetivo in problem.state_objetivo:
                if metrica == 'valor':
                    valor_child = child.valores[objetivo.name]
                    valor_mejor = mejor.valores[objetivo.name]
                    if (criterio == 'menor' and valor_child < valor_mejor):
                        mejor = child
                    elif (criterio == 'mayor' and valor_child > valor_mejor):
                        mejor = child
                elif metrica == 'heuristica':
                    heuristica_child = child.heuristicas[objetivo.name]
                    heuristica_mejor = mejor.heuristicas[objetivo.name]
                    if (criterio == 'menor' and heuristica_child < heuristica_mejor):
                        mejor = child
                    elif (criterio == 'mayor' and heuristica_child > heuristica_mejor):
                        mejor = child
                elif metrica == 'costo':
                    costo_camino_child = problem.costo_camino(child)
                    costo_camino_mejor = problem.costo_camino(mejor)
                    if (criterio == 'menor' and costo_camino_child < costo_camino_mejor):
                        mejor = child
                    elif (criterio == 'mayor' and costo_camino_child > costo_camino_mejor):
                        mejor = child
        return mejor
