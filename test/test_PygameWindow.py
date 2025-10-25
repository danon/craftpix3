from hex.core.Color import Color
from hex.core.port import ForRenderingView
from hex.PygameEngine import PygameEngine
from hex.PygameWindow import PygameWindow

def test_background(engine: PygameEngine):
    render: ForRenderingView = PygameWindow(engine)
    render.fill_background(Color(30, 31, 34))
    assert engine.pixel_color(0, 0) == Color(30, 31, 34)
