class GameWorld:
    def __init__(self):
        self.player_x = 0
        self.__left = False
        self.__right = False

    def player_move_right(self, active: bool):
        self.__right = active

    def player_move_left(self, active: bool):
        self.__left = active

    def tick(self):
        self.player_x += self.__velocity_x()

    def __velocity_x(self) -> int:
        if self.__left == self.__right:
            return 0
        return 1 if self.__right else -1
