class GameWorld:
    def __init__(self):
        self.player_x = 0

    def player_move_right(self):
        self.player_x += 1

    def player_move_left(self):
        self.player_x -= 1
