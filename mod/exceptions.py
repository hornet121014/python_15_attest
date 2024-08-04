class NegativeValueError(Exception):
    def __init__(self, message="Ширина и высота должны быть положительными числами"):
        self.message = message
        super().__init__(self.message)


class MissingWidthError(Exception):
    def __init__(self, message="Ширина должна быть указана"):
        self.message = message
        super().__init__(self.message)
