class Problem:
    def __init__(self, initial_status, target_status,
                 actions, price=None, heuristicas=None):
        self.initial_status = initial_status
        self.target_status = target_status
        self.actions = actions
        self.price = price
        self.infinito = 9999999
        self.heuristicas = heuristicas

        if not self.price:
            self.price = {}
            for status in self.actions.keys():
                self.price[status] = {}
                for action in self.actions[status].keys():
                    self.price[status][action] = 1

        if not self.heuristicas:
            self.heuristicas = {}
            for status in self.actions.keys():
                self.heuristicas[status] = {}
                for objetivo in self.target_status:
                    self.heuristicas[status][objetivo] = self.infinito

    def __str__(self):
        msg = "status inicial: {0} -> Objetivos: {1}"
        return msg.format(self.initial_status.name, self.target_status)

    def is_target(self, status):
        return status in self.target_status

    def result(self, status, action):
        if status.name not in self.actions.keys():
            return None
        actions_status = self.actions[status.name]
        if action.name not in actions_status.keys():
            return None
        return actions_status[action.name]

    def price_action(self, status, action):
        if status.name not in self.price.keys():
            return self.infinito
        price_status = self.price[status.name]
        if action.name not in price_status.keys():
            return self.infinito
        return price_status[action.name]

    def price_camino(self, nodo):
        total = 0
        while nodo.padre:
            total += self.price_action(nodo.padre.status, nodo.action)
            nodo = nodo.padre
        return total
