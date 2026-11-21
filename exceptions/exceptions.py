class ParserException(Exception):
    def __init__(self, message = "Unknown parser exception!") -> None:
        super().__init__(message)
        self.message = message
