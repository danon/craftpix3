from enum import Enum

class Stance(Enum):
    Idle = 0
    Walk = 1

class Turn(Enum):
    Left = 0
    Right = 1

class GameWorld:
    def __init__(self):
        self.player = Figure()
        self.__left = False
        self.__right = False

    def player_move_right(self, active: bool):
        self.__right = active

    def player_move_left(self, active: bool):
        self.__left = active

    def tick(self):
        self.player.update(self.__velocity_x())

    def __velocity_x(self) -> int:
        if self.__left == self.__right:
            return 0
        return 1 if self.__right else -1

class Figure:
    def __init__(self):
        self.x = 0
        self.turn = Turn.Right
        self.stance = Stance.Idle

    def update(self, velocity_x: int):
        self.x += velocity_x
        self.__update_turn(velocity_x)
        self.__update_stance(velocity_x)

    def __update_turn(self, velocity_x):
        if velocity_x > 0:
            self.turn = Turn.Right
        if velocity_x < 0:
            self.turn = Turn.Left

    def __update_stance(self, velocity_x: int) -> None:
        if velocity_x == 0:
            self.stance = Stance.Idle
        else:
            self.stance = Stance.Walk
