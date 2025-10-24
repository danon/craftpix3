from pix.sprite import Sprite

def test_sprite_returns_frame():
    sprite = Sprite(['frame1.png'])
    assert sprite.frame(0) == 'frame1.png'

def test_sprite_cycles_frames():
    sprite = Sprite(['frame1.png', 'frame2.png', 'frame3.png'])
    assert sprite.frame_cycle(4) == 'frame2.png'

# using file system:
# read structure of obstacle
# load frames
# expose them as nice interface
# render them in pygame


# Later:
# we will want a structure, that:
# holds multiple animations
# icon or avatar
# projectiles
