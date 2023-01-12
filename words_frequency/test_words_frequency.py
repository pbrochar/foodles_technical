import pytest

from .words_frequency import words_frequency



def test_words_frequency():
    assert words_frequency("test toto test toto a b", 3) == [
        ("test", 2),
        ("toto", 2),
        ("a", 1),
    ]

    assert words_frequency("baz bar foo foo zblah zblah zblah baz toto bar", 3) == [
        ("zblah", 3),
        ("bar", 2),
        ("baz", 2),
    ]
