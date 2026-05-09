class PlatoDuplicadoError(Exception):
    def __init__(self, mensaxe):
        super().__init__(mensaxe)