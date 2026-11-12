# Wordstat — Word Frequency Counter

## Overview

Wordstat is a Python command-line application that reads a text file and displays the most frequently occurring words.

It uses Python's standard library and does not require additional packages to run the application.

## Features

- Counts word occurrences in a text file.
- Treats uppercase and lowercase versions of a word as the same word.
- Handles punctuation and Unicode text.
- Displays the top N words requested by the user.
- Sorts words by frequency in descending order and alphabetically when frequencies are tied.
- Displays a clear error message when the input file does not exist.
- Handles empty files without errors.

## Requirements

- Python 3
- pytest for running the automated tests

## Usage

Run the program with a text file:

```bash
python wordstat.py sample.txt
```

Display only the top three words:

```bash
python wordstat.py sample.txt --top 3
```

The `-n` option is also supported:

```bash
python wordstat.py sample.txt -n 2
```

If the file does not exist, the program displays an error message.

## Running the Tests

Run the automated test suite:

```bash
python -m pytest -v
```

The tests cover repeated words, case-insensitive counting, punctuation, empty files, Unicode text, very long lines, top N results, and missing files.

## Project Files

- `wordstat.py` — application code.
- `test_wordstat.py` — automated tests.
- `sample.txt` — sample input file.
- `README.md` — project documentation.

## Learning Reflection

This project helped me practise Python functions, regular expressions, dictionaries and counters, command-line argument parsing, file handling, exception handling, and automated testing with pytest.

I also learned how to use AI assistance to understand errors, improve my code, and test edge cases.
