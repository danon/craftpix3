from hex.CliTerminal import CliTerminal
from hex.core.port import ForRenderingFrames
from test.helper.captured_output import captured_output

class Test_CliTerminal:
    def test_renders_frames(self):
        terminal: ForRenderingFrames = CliTerminal()
        assert captured_output(lambda: terminal.render_frames(['frame1.png'])) == "['frame1.png']"
