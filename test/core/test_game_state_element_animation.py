from hex.core.obstacle import Obstacle
from hex.core.SpriteLoader import Sprite

def test_element_has_first_frame():
    obstacle = Obstacle(Sprite(['frame1.png', 'frame2.png']))
    assert obstacle.frame() == 'frame1.png'

def test_initiated_element_has_second_frame():
    obstacle = Obstacle(Sprite(['frame1.png', 'frame2.png']))
    obstacle.initiate()
    obstacle.tick()
    assert obstacle.frame() == 'frame2.png'

def test_initiated_element__after_game_ticks_twice__has_third_frame():
    obstacle = Obstacle(Sprite(['frame1.png', 'frame2.png', 'frame3.png']))
    obstacle.initiate()
    obstacle.tick()
    obstacle.tick()
    assert obstacle.frame() == 'frame3.png'

def test_not_initiated_element__after_game_ticks__has_first_frame():
    obstacle = Obstacle(Sprite(['frame1.png', 'frame2.png']))
    obstacle.tick()
    assert obstacle.frame() == 'frame1.png'

def test_initiated_element__after_last_frame__has_first_frame():
    obstacle = Obstacle(Sprite(['frame1.png', 'frame2.png', 'frame3.png']))
    obstacle.initiate()
    obstacle.tick()
    obstacle.tick()
    obstacle.tick()
    assert obstacle.frame() == 'frame1.png'

def test_initiated_element__after_last_frame__when_game_ticks__has_first_frame():
    obstacle = Obstacle(Sprite(['frame1.png', 'frame2.png', 'frame3.png']))
    obstacle.initiate()
    obstacle.tick()
    obstacle.tick()
    obstacle.tick()
    obstacle.tick()
    assert obstacle.frame() == 'frame1.png'

def test_initiated_element__after_initiating_again__does_not_cancel_animation():
    obstacle = Obstacle(Sprite(['frame1.png', 'frame2.png', 'frame3.png']))
    obstacle.initiate()
    obstacle.tick()
    obstacle.initiate()
    obstacle.tick()
    assert obstacle.frame() == 'frame3.png'
