import pytest
from domain.objects.author_2 import Author, InvalidAuthorError

def test_valid_author():
    a = Author("Onyx")
    assert str(a) == "Onyx"

def test_blank_author_raises():
    with pytest.raises(InvalidAuthorError):
        Author("  ")

def test_too_long_author_raises():
    with pytest.raises(InvalidAuthorError):
        Author("A" * 51)
