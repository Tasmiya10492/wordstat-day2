
import pytest

from wordstat import count_words, get_top_words, main

def test_repeated_words():
    assert count_words("cat dog cat") == {
        "cat": 2,
        "dog": 1,
    }


def test_case_insensitive_counting():
    assert count_words("Python PYTHON python") == {
        "python": 3,
    }


def test_punctuation():
    assert count_words("hello, hello! world.") == {
        "hello": 2,
        "world": 1,
    }


def test_empty_file(tmp_path, capsys):
    file_path = tmp_path / "empty.txt"
    file_path.write_text("", encoding="utf-8")

    main([str(file_path)])

    assert capsys.readouterr().out == "No words found.\n"


def test_unicode_text():
    assert count_words("café CAFÉ naïve") == {
        "café": 2,
        "naïve": 1,
    }


def test_very_long_line():
    text = ("apple " * 100_000) + "banana"

    assert count_words(text) == {
        "apple": 100_000,
        "banana": 1,
    }


def test_top_n_words():
    assert get_top_words("banana apple banana apple cherry", 2) == [
        ("apple", 2),
        ("banana", 2),
    ]


def test_missing_file(tmp_path, capsys):
    file_path = tmp_path / "missing.txt"

    with pytest.raises(SystemExit) as error:
        main([str(file_path)])

    assert error.value.code == 2
    assert f"file not found: {file_path}" in capsys.readouterr().err
