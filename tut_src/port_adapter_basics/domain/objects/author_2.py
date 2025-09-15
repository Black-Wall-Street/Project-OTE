class InvalidAuthorError(Exception):
    pass

class Author:
    def __init__(self, name: str):
        name = name.strip()
        if not name:
            raise InvalidAuthorError("Author name cannot be empty.")
        if len(name) > 50:
            raise InvalidAuthorError("Author name cannot exceed 50 characters.")
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    def __str__(self):
        return self._name
