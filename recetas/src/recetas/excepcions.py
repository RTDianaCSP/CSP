class PlatoDuplicadoError(Exception): #excepcion propia

    def __init__(self, mensaje="O plato xa existe no menú"):
        super().__init__(mensaje)