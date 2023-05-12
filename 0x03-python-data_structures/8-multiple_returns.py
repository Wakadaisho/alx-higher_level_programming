#!/usr/bin/python3
def multiple_returns(sentence):
    return (len(sentence), len(sentence) and sentence[0] or None)
