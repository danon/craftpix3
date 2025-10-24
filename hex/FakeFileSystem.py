from hex.core.port import ForReadingSpriteFiles

class FakeFileSystem(ForReadingSpriteFiles):
    def list_files(self, path: str) -> list[str]:
        return []

    def root(self) -> str:
        return '/root'
