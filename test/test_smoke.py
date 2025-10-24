from hex.__main__ import main
from test.helper.captured_output import captured_output

def test_smoke():
    assert captured_output(lambda: main()) == "['resource/sprite1.png', 'resource/sprite2.png']"
