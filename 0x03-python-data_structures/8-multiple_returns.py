#!/usr/bin/python3
def multiple_returns(sentence):
    """Return a pair of the length of a sentence and the first letter

    Args:
        sentence: string to process

    Return:
        Pair of length of a sentence and a first letter
    """
    return (len(sentence), len(sentence) and sentence[0] or None)
