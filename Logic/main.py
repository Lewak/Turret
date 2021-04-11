import atexit
from peripherals import Peripherals
from state_machine import StateMachine
from sleep_state import SleepState
from peripherals import Peripherals

try:
    Peripherals.initialise()
    print("Attention evacuation emergency all personnel must evacuate immediately")
    Peripherals.motorHorizontal.setPosition(90)

    stateMachine = StateMachine()
    stateMachine.set_inital_state(SleepState())
    stateMachine.run()
except KeyboardInterrupt:
    pass
finally:
    Peripherals.destroy()
    print("Shutdown complete")
