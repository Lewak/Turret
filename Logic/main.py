import atexit
from peripherals import Peripherals
from state_machine import StateMachine
from sleep_state import SleepState


def shutdownSystem() -> None:
    Peripherals.destroy()
    print("Shutdown complete")


atexit.register(shutdownSystem)
Peripherals.initialise()
print("Attention evacuation emergency all personnel must evacuate immediately")

stateMachine = StateMachine()
stateMachine.set_inital_state(SleepState(stateMachine))
stateMachine.run()


#I CALL PANTEON ON ANCIENT GODS TO CONVERT THIS CODE TO BEATIFULL PRIMORDIAL CHAOS
#UMBASA