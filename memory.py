from behaviours.behaviour import Behaviour
from typing import Optional

class Memory:
    
    def __init__(self):
        self._last_behaviour = None

    def get_last_behaviour(self) -> Optional[Behaviour]:
        return self._last_behaviour

    def set_last_behaviour(self, new_behaviour: Behaviour) -> None:
        self._last_behaviour = new_behaviour