from hex.core.GameWorld import GameWorld, PlayerStance

def test_player_initially_is_at_x_0():
    world = GameWorld()
    assert world.player_x == 0

def test_when_player_moves_right_he_is_at_x_1():
    world = GameWorld()
    world.player_move_right(True)
    world.tick()
    assert world.player_x == 1

def test_when_player_moves_left_he_is_at_x_minus_1():
    world = GameWorld()
    world.player_move_left(True)
    world.tick()
    assert world.player_x == -1

def test_player_keeps_moving_right_while_right_is_active():
    world = GameWorld()
    world.player_move_right(True)
    world.tick()
    world.tick()
    assert world.player_x == 2

def test_player_stops_moving_right_when_right_is_not_active():
    world = GameWorld()
    world.player_move_right(True)
    world.tick()
    world.player_move_right(False)
    world.tick()
    assert world.player_x == 1

def test_player_stops_moving_left_when_left_is_not_active():
    world = GameWorld()
    world.player_move_left(True)
    world.tick()
    world.player_move_left(False)
    world.tick()
    assert world.player_x == -1

def test_play_does_not_move_when_both_keys_are_active():
    world = GameWorld()
    world.player_move_left(True)
    world.player_move_right(True)
    world.tick()
    assert world.player_x == 0

def test_given_two_keys_are_held_when_left_is_released_the_player_moves_right():
    # given
    world = GameWorld()
    world.player_move_left(True)
    world.player_move_right(True)
    # when
    world.player_move_left(False)
    # then
    world.tick()
    assert world.player_x == 1

def test_given_two_keys_are_held_when_right_is_released_the_player_moves_left():
    # given
    world = GameWorld()
    world.player_move_left(True)
    world.player_move_right(True)
    # when
    world.player_move_right(False)
    # then
    world.tick()
    assert world.player_x == -1

def test_given_incorrectly_sending_up_the_player_does_not_move():
    # given
    world = GameWorld()
    # when
    world.player_move_right(False)
    # then
    world.tick()
    assert world.player_x == 0

def test_given_stationary_player__its_stance_is_idle():
    world = GameWorld()
    assert world.player_stance == PlayerStance.Idle

def test_given_a_moving_player__its_stance_is_walk():
    world = GameWorld()
    world.player_move_right(True)
    assert world.player_stance == PlayerStance.Walk

def test_player_initially_looks_right():
    world = GameWorld()
    assert world.looks_right

def test_player_after_moving_left__player_looks_left():
    world = GameWorld()
    world.player_move_left(True)
    world.tick()
    assert not world.looks_right

def test_player_after_moving_right__player_looks_right():
    world = GameWorld()
    world.player_move_left(True)
    world.player_move_left(False)
    world.tick()
    world.player_move_right(True)
    world.tick()
    assert world.looks_right

def test_player_maintains_right_turn():
    world = GameWorld()
    world.player_move_right(True)
    world.tick()
    world.player_move_right(False)
    world.tick()
    assert world.looks_right

def test_player_maintains_left_turn():
    world = GameWorld()
    world.player_move_left(True)
    world.tick()
    world.player_move_left(False)
    world.tick()
    assert not world.looks_right
