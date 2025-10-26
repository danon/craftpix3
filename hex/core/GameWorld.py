from enum import Enum

class PlayerStance(Enum):
    Idle = 0
    Walk = 1

class GameWorld:
    def __init__(self):
        self.player_x = 0
        self.__left = False
        self.__right = False
        self.looks_right = True

    def player_move_right(self, active: bool):
        self.__right = active

    def player_move_left(self, active: bool):
        self.__left = active

    def tick(self):
        velocity = self.__velocity_x()
        if velocity > 0:
            self.looks_right = True
        if velocity < 0:
            self.looks_right = False
        self.player_x += velocity

    @property
    def player_stance(self) -> PlayerStance:
        if self.__velocity_x() == 0:
            return PlayerStance.Idle
        return PlayerStance.Walk

    def __velocity_x(self) -> int:
        if self.__left == self.__right:
            return 0
        return 1 if self.__right else -1
