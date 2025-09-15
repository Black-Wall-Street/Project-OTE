import pytest
from domain.objects.content_3 import Content, InvalidContentError

def test_valid_content():
    c = Content("Great video!")
    assert str(c) == "Great video!"

def test_blank_content_raises():
    with pytest.raises(InvalidContentError):
        Content("   ")
