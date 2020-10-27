import time


class State:
    def __init__(self):
        pass
    def routine(self) -> 'State':
        pass

    def enter(self) -> None:
        pass

    def leave(self) -> None:
        pass

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
            proceedCheck = self.currentState.routine()
            if proceedCheck is not None:
                self.switch_state(proceedCheck)
            time.sleep(1/30)


