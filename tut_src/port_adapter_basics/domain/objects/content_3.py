class InvalidContentError(Exception):
    pass

class Content:
    def __init__(self, value: str):
        value = value.strip()
        if not value:
            raise InvalidContentError("Comment content cannot be empty.")
        self._value = value

    @property
    def value(self) -> str:
        return self._value

    def __str__(self):
        return self._value
