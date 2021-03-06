import atexit
from peripherals import Peripherals
from state_machine import StateMachine
from sleep_state import SleepState


try:
    Peripherals.initialise()
    print("Attention evacuation emergency all personnel must evacuate immediately")

    stateMachine = StateMachine()
    stateMachine.set_inital_state(SleepState())
    stateMachine.run()
except KeyboardInterrupt:
    pass
finally:
    Peripherals.destroy()
    print("Shutdown complete")
