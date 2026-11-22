class ParserException(Exception):
    def __init__(self, message = "Unknown parser exception!", line: int = 0) -> None:
        super().__init__(message)
        self.message = message
        self.line = line
