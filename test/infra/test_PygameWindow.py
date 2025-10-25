from hex.core.Color import Color
from hex.core.port import ForRenderingView
from hex.infra.PygameEngine import PygameEngine
from hex.infra.PygameWindow import PygameWindow
from test.helper.resource import resource

res = resource(__file__)

def test_background(engine: PygameEngine):
    render: ForRenderingView = PygameWindow(engine)
    render.fill_background(Color(30, 31, 34))
    assert engine.pixel_color(0, 0) == Color(30, 31, 34)

def test_renders_frame_on_background(engine: PygameEngine):
    render: ForRenderingView = PygameWindow(engine)
    render.fill_background(Color(255, 255, 34))
    render.draw_frame(res('1.sprite.png'), 0, 0)
    engine.capture(res('1.actual.png'))
    assert images_equal(
        res('1.actual.png'),
        res('1.expected.png'))

def test_renders_frames_next_to_each_other(engine: PygameEngine):
    render: ForRenderingView = PygameWindow(engine)
    render.fill_background(Color(255, 255, 34))
    render.draw_frame(res('2.sprite.png'), 0, 0)
    render.draw_frame(res('2.sprite.png'), 32, 64)
    render.draw_frame(res('2.sprite.png'), 64, 128)
    engine.capture(res('2.actual.png'))
    assert images_equal(
        res('2.actual.png'),
        res('2.expected.png'))

def images_equal(actual: str, expected: str) -> bool:
    with open(actual, mode='rb') as a:
        with open(expected, mode='rb') as b:
            return a.read() == b.read()
