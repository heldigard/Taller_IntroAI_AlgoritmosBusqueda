import Action


class State:
    def __init__(self, name, actions: list[Action]):
        self.name = name
        self.actions = actions

    def __str__(self):
        return self.name
