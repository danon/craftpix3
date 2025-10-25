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
