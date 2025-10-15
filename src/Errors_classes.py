class BracketsError(Exception):
    """Ошибка при неправильной расстановке ошибок"""
    def __init__(self, message="Ошибка"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


class IvalidCharacterError(Exception):
    """Ошибка при введенном недопустимом символе"""
    def __init__(self, message="Ошибка"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


class CalculateError(Exception):
    def __init__(self, message="Ошибка"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


class FatalError(Exception):
    def __init__(self, message="Ошибка"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


class OpersMoreNumsError(Exception):
    def __init__(self, message="Ошибка"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'
