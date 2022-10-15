"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""


def frequencies(items):
    item2 = list(map(str, items))
    frequencies = {x: item2.count(x) for x in item2}
    return frequencies
