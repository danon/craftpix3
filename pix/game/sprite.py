class Sprite:
    def __init__(self, frames: list[str]):
        self.frames = frames

    def frame(self, index: int) -> str:
        return self.frames[index]

    def frame_cycle(self, index: int) -> str:
        return self.frame(index % len(self.frames))
