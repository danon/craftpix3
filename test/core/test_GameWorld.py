from hex.core.GameWorld import GameWorld

def test_player_initially_is_at_x_0():
    world = GameWorld()
    assert world.player_x == 0

def test_when_player_moves_right_he_is_at_x_1():
    world = GameWorld()
    world.player_move_right()
    assert world.player_x == 1

def test_when_player_moves_left_he_is_at_x_minus_1():
    world = GameWorld()
    world.player_move_left()
    assert world.player_x == -1
