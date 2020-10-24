from state_machine import StateMachine


class State:

    def __init__(self, stateMachine: StateMachine):
        self.stateMachine = stateMachine

    def routine(self) -> 'State':
        pass

    def enter(self) -> None:
        pass

    def leave(self) -> None:
        pass
