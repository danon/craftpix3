from hex.core.Color import Color
from hex.core.port import ForRenderingView
from hex.PygameEngine import PygameEngine
from hex.PygameWindow import PygameWindow
from test.helper.resource import resource

res = resource(__file__)

def test_background(engine: PygameEngine):
    render: ForRenderingView = PygameWindow(engine)
    render.fill_background(Color(30, 31, 34))
    assert engine.pixel_color(0, 0) == Color(30, 31, 34)

def test_renders_frame_on_background(engine: PygameEngine):
    render: ForRenderingView = PygameWindow(engine)
    render.fill_background(Color(255, 255, 34))
    render.draw_frame(res('sprite.png'))
    engine.capture(res('actual.png'))
    assert images_equal(
        res('actual.png'),
        res('expected.png'))

def images_equal(actual: str, expected: str) -> bool:
    with open(actual, mode='rb') as a:
        with open(expected, mode='rb') as b:
            return a.read() == b.read()
