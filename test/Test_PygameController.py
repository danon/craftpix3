from hex.core.port import WindowEvent
from hex.PygameController import PygameController
from hex.PygameEngine import PygameEngine

class Test_PygameController:
    def test_polls_empty(self, engine: PygameEngine):
        controller = PygameController(engine)
        events = controller.poll_events()
        assert events == []

    def test_polls_click(self, engine: PygameEngine):
        controller = PygameController(engine)
        engine.click()
        [event] = controller.poll_events()
        assert event == WindowEvent.Click

    def test_polls_close(self, engine: PygameEngine):
        controller = PygameController(engine)
        engine.close()
        [event] = controller.poll_events()
        assert event == WindowEvent.Close
