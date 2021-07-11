#!/usr/bin/env python
from itertools import permutations

def get_perms(letters: list[str]) -> list[tuple[str]]:
    """
    Gets all n-letter permutations using the letters in the input string
    where n is the number of letters.
    """
    # # My algorithm attempt (slower than itertools):

    # prev_perms = [[letters[0]]]
    # for idx, letter in enumerate(letters[1:]):
    #     cur_perms = []
    #     for prev in prev_perms:
    #         for i in range(idx+2):
    #             prev_copy = prev[:]
    #             prev_copy.insert(i, letter)
    #             cur_perms.append(prev_copy)
    #     prev_perms = cur_perms
    # return cur_perms

    perms = permutations(letters)

    return list(perms)

def convert_to_strings(tups: list[tuple[str]]) -> list[str]:
    """Converts each string tuple to strings in the given list."""
    strings = []

    for t in tups:
        strings.append(''.join(t))

    return strings

def get_words(str_list: list[str]) -> list[str]:
    """Reads from words text file and returns list of matching words from permutations."""
    with open('words.txt') as f:
        ref_words = f.read().splitlines()

    word_length = len(str_list[0])
    filtered_ref_words = [word for word in ref_words if len(word) == word_length]

    str_set = set(str_list)
    words = str_set.intersection(filtered_ref_words)

    return list(words)

def solve_jumble(jumbled_word: str) -> list[str]:
    """
    Solves a Jumble puzzle based on given input string.
    Input must be between 2 and 10 letters long.
    """
    if (not isinstance(jumbled_word, str) or
        not jumbled_word.isalpha() or
        len(jumbled_word) < 2 or
        len(jumbled_word) > 10):
        return [] 

    jum_letters = list(jumbled_word.lower())
    perms = get_perms(jum_letters)
    perm_strings = convert_to_strings(perms)
    words = get_words(perm_strings)
    return sorted(words)
