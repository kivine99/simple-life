class Energy:
    def __init__(self, max_energy: float, move_energy_lost: float, eat_energy_gained: float):
        self._max_energy = max_energy
        self._curr_energy = max_energy
        self._move_energy_lost = move_energy_lost
        self._eat_energy_gained = eat_energy_gained

    def get_max_energy(self) -> float:
        return self._max_energy

    def get_move_energy_lost(self) -> float:
        return self._move_energy_lost

    def get_curr_energy(self) -> float:
        return self._curr_energy

    def get_eat_energy_gained(self) -> float:
        return self._eat_energy_gained

    def increase_energy(self, energy_amount: float) -> None:
        self._curr_energy = min(self._curr_energy+energy_amount, self._max_energy)

    def decrease_energy(self, energy_amount: float) -> None:
        self._curr_energy -= energy_amount

    