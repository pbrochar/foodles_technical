import pytest

from .words_frequency import words_frequency


def test_words_frequency_raise_value_error():
    with pytest.raises(ValueError):
        words_frequency("test toto", -1)


def test_words_frequency():
    assert words_frequency("test toto test toto a b", 3) == [
        ("toto", 2),
        ("test", 2),
        ("b", 1),
    ]
