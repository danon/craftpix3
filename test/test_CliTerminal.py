from hex.CliTerminal import CliTerminal
from hex.core.port import ForRenderingFrames
from test.helper.captured_output import captured_output

def test_renders_frames():
    terminal: ForRenderingFrames = CliTerminal()
    assert captured_output(lambda: terminal.render_frames(['frame1.png'])) == "['frame1.png']"
