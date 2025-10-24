from hex.core.Application import ForReadingSpriteFiles

class FakeFileSystem(ForReadingSpriteFiles):
    def root(self) -> str:
        return '/root'
