import logging
import sys

log = logging.getLogger("my-logger")
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler(sys.stdout))

def substring_anagrams(s: str, p: str) -> int:
    p_len, p_freq = len(p), freq(p)
    s_len = len(s)

    if s_len < p_len:
        return 0

    left, right = 0, 0
    sliding_freq = [0] * 26
    ord_a = ord('a')

    while right < p_len - 1:
        sliding_freq[ord(s[right]) - ord_a] += 1
        right += 1

    count = 0
    while right < s_len:
        sliding_freq[ord(s[right]) - ord_a] += 1
        log.debug(f"Sliding freq: {sliding_freq}, P freq: {p_freq}")
        if sliding_freq == p_freq:
            count += 1
        sliding_freq[ord(s[left]) - ord_a] -= 1
        left += 1
        right +=1        

    return count


def freq(s: str) -> list[int]:
    freq = [0] * 26
    ord_a = ord('a')
    for char in s:
        idx = ord(char) - ord_a
        freq[idx] += 1
    return freq

def test_frequency_map():
    assert freq("") == [0] * 26
    assert freq("a") == [1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                    0, 0, 0, 0, 0, 0 ]
    assert freq("abza") == [ 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 
                                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                                        0, 0, 0, 0, 0, 1 ]


def test_substring_anagrams():
    assert substring_anagrams("a", "ab") == 0
    assert substring_anagrams("ara", "ara") == 1 # "ara" is an anagram of "ara"
    assert substring_anagrams("carate", "ara") == 1 # "ara" is an anagram of "ara"
    assert substring_anagrams("caraate", "ara") == 2 # "ara" and "raa" are anagrams of "ara"
