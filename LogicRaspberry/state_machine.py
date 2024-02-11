import time
from peripherals import Peripherals


class State:
    def routine(self) -> 'State':
        pass

    def enter(self) -> None:
        pass

    def leave(self) -> None:
        pass


class StateMachine:
    def __init__(self):
        self.currentState = None

    def set_initial_state(self, initialState: State):
        self.currentState = initialState

    def switch_state(self, nextState: 'State') -> None:
        self.currentState.leave()
        self.currentState = nextState
        self.currentState.enter()

    def run(self) -> None:
        # while not Peripherals.button.isPressed():
        while True:
            nextState = self.currentState.routine()
            if nextState is not self.currentState:
                self.switch_state(nextState)
            time.sleep(1/30)
