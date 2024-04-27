import Node
import State


class Problem:
    def __init__(self, initial_state: State, target_state: State,
                 actions: dict, price: dict = None, heuristics: dict = None):
        self.initial_state = initial_state
        self.target_state = target_state
        self.actions = actions
        self.price = price
        self.infinito = 9999999
        self.heuristics = heuristics

        if not self.price:
            self.price = {}
            for state in self.actions.keys():
                self.price[state] = {}
                for action in self.actions[state].keys():
                    self.price[state][action] = 1

        if not self.heuristics:
            self.heuristics = {}
            for state in self.actions.keys():
                self.heuristics[state] = {}
                for objetivo in self.target_state:
                    self.heuristics[state][objetivo] = self.infinito

    def __str__(self):
        msg = "state inicial: {0} -> Objetivos: {1}"
        return msg.format(self.initial_state.name, self.target_state)

    def is_target(self, state):
        return state in self.target_state

    def result(self, state, action):
        if state.name not in self.actions.keys():
            return None
        actions_state = self.actions[state.name]
        if action.name not in actions_state.keys():
            return None
        return actions_state[action.name]

    def price_action(self, state, action):
        if state.name not in self.price.keys():
            return self.infinito
        price_state = self.price[state.name]
        if action.name not in price_state.keys():
            return self.infinito
        return price_state[action.name]

    def path_price(self, node: Node):
        total = 0
        while node.father:
            total += self.price_action(node.father.state, node.action)
            node = node.father
        return total
