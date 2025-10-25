from hex.core.GameState import Element, GameState
from hex.core.SpriteLoader import Sprite

def test_element_has_first_frame():
    game = GameState()
    game.element = Element(Sprite(['frame1.png', 'frame2.png']))
    assert game.element.frame() == 'frame1.png'

def test_initiated_element_has_second_frame():
    game = GameState()
    game.element = Element(Sprite(['frame1.png', 'frame2.png']))
    game.element.initiate()
    game.tick()
    assert game.element.frame() == 'frame2.png'

def test_initiated_element__after_game_ticks_twice__has_third_frame():
    game = GameState()
    game.element = Element(Sprite(['frame1.png', 'frame2.png', 'frame3.png']))
    game.element.initiate()
    game.tick()
    game.tick()
    assert game.element.frame() == 'frame3.png'

def test_not_initiated_element__after_game_ticks__has_first_frame():
    game = GameState()
    game.element = Element(Sprite(['frame1.png', 'frame2.png']))
    game.tick()
    assert game.element.frame() == 'frame1.png'

def test_initiated_element__after_last_frame__has_first_frame():
    game = GameState()
    game.element = Element(Sprite(['frame1.png', 'frame2.png', 'frame3.png']))
    game.element.initiate()
    game.tick()
    game.tick()
    game.tick()
    assert game.element.frame() == 'frame1.png'

def test_initiated_element__after_last_frame__when_game_ticks__has_first_frame():
    game = GameState()
    game.element = Element(Sprite(['frame1.png', 'frame2.png', 'frame3.png']))
    game.element.initiate()
    game.tick()
    game.tick()
    game.tick()
    game.tick()
    assert game.element.frame() == 'frame1.png'

def test_initiated_element__after_initiating_again__does_not_cancel_animation():
    game = GameState()
    game.element = Element(Sprite(['frame1.png', 'frame2.png', 'frame3.png']))
    game.element.initiate()
    game.tick()
    game.element.initiate()
    game.tick()
    assert game.element.frame() == 'frame3.png'
