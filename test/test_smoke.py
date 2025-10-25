from hex.__main__ import main
from test.helper.captured_output import captured_output

def test_smoke():
    output = captured_output(lambda: main())
    line, *_ = output.split("\n")
    assert line == "['resource/sprite1.png', 'resource/sprite2.png']"
