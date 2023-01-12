from typing import List, Tuple
from collections import Counter

def words_frequency(sentence: str, n: int) -> List[Tuple[str, int]]:
    """
    Function who returns a list of size `n` where each element contains a word and and the frequency of that word in `sentence`
    This list should is sort by decreasing frequency and alphabetical order in case of tie.
    """


    splitted_sentence = sentence.split()
    splitted_sentence.sort()
    return Counter(splitted_sentence).most_common(n)

