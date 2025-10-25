from hex.core.port import ForRenderingView
from hex.PygameEngine import PygameEngine
from hex.PygameWindow import PygameWindow

class Test_PygameWindow:
    def test_background(self, engine: PygameEngine):
        render: ForRenderingView = PygameWindow(engine)
        render.fill_background(30, 31, 34)
        assert engine.pixel_color(0, 0) == (30, 31, 34)
