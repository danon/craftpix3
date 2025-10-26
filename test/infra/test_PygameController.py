from hex.core.port import WindowEvent
from hex.infra.PygameController import PygameController
from hex.infra.PygameEngine import PygameEngine

def test_polls_empty(engine: PygameEngine):
    controller = PygameController(engine)
    events = controller.poll_events()
    assert events == []

def test_polls_click(engine: PygameEngine):
    controller = PygameController(engine)
    engine.click()
    [event] = controller.poll_events()
    assert event == WindowEvent.Click

def test_polls_close(engine: PygameEngine):
    controller = PygameController(engine)
    engine.close()
    [event] = controller.poll_events()
    assert event == WindowEvent.Close

def test_polls_arrows_down(engine: PygameEngine):
    controller = PygameController(engine)
    engine.right_down()
    engine.left_down()
    events = controller.poll_events()
    assert events == [
        WindowEvent.RightDown,
        WindowEvent.LeftDown,
    ]

def test_polls_arrows_up(engine: PygameEngine):
    controller = PygameController(engine)
    engine.right_up()
    engine.left_up()
    events = controller.poll_events()
    assert events == [
        WindowEvent.RightUp,
        WindowEvent.LeftUp,
    ]
