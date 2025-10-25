from hex.core.port import ForReadingUserInput, WindowEvent

class QuitAfterPolls(ForReadingUserInput):
    def __init__(self, polls: int):
        self.__polls = polls

    def poll_events(self) -> list[WindowEvent]:
        self.__polls -= 1
        if self.__polls > 0:
            return []
        return [WindowEvent.Close]
