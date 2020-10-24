from state import State
import time


class StateMachine:
    def __init__(self):
        self.currentState = None

    def set_inital_state(self, initialState: State):
        self.currentState = initialState

    def switch_state(self, nextState: 'State') -> None:
        self.currentState.leave()
        self.currentState = nextState
        self.currentState.enter()

    def run(self) -> None:
        while True:
            self.currentState.routine()
            time.sleep(1/30)
