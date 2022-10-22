from src.counter import count_ocurrences

PATH = "src/jobs.csv"
WORD = "python"
OCCURENCES = 1639


def test_counter():
    ocurrences = count_ocurrences(PATH, WORD.lower())
    assert ocurrences == OCCURENCES
