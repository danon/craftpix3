from hex.core.port import ForRenderingFrames

class SpyRender(ForRenderingFrames):
    def __init__(self):
        self.frames = None

    def render_frames(self, frames: list[str]):
        self.frames = frames
