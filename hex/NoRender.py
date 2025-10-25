from hex.core.port import ForRenderingFrames

class NoRender(ForRenderingFrames):
    def render_frames(self, frames: list[str]):
        pass
