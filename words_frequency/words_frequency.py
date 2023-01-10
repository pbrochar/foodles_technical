from typing import List, Tuple
import operator


def words_frequency(sentence: str, n: int) -> List[Tuple[str, int]]:
    """
    Function who returns a list of size `n` where each element contains a word and and the frequency of that word in `sentence`
    This list should is sort by decreasing frequency and alphabetical order in case of tie.
    """
    if n < 0:
        raise ValueError("n can't be negative")

    splitted_sentence = sentence.split()
    unique_words = set(splitted_sentence)

    count = [(word, splitted_sentence.count(word)) for word in unique_words]
    count.sort(reverse=True, key=lambda a: (a[1], a[0]))
    return count[0:n]
