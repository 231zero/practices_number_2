def brutforce(words: list[str]):
    if not is_words_correct_type(words):
        raise TypeError
    
    max_length = 0
    answer = []
    for word1 in words:
        for word2 in words:
            if word1 == word2 or word1 == "" or word2 == "":
                continue
            min_len = max_length
            max_len = min(len(word2), len(word2))
            for pref in range(max_len, min_len, -1):
                if word2.endswith(word1[:pref]):
                    max_length = pref
                    answer = [word1, word2]
                    break
    return max_length, answer


def fast(words: list[str]):
    if not is_words_correct_type(words):
        raise TypeError

    answer_length = 0
    answer = []
    prefixes = {}
    for word in words:
        for i in range(1, len(word) + 1):
            pref = word[:i]
            if pref not in prefixes:
                prefixes[pref] = set()
            prefixes[pref].add(word)

    for word2 in words:
        substr_found = False
        min_len = answer_length
        max_len = len(word2)
        for i in range(max_len, min_len, -1):
            substr = word2[-i:]
            if substr in prefixes:
                for word1 in prefixes[substr]:
                    if word1 == word2:
                        continue
                    answer_length = i
                    answer = [word1, word2]
                    break
            if substr_found:
                break

    return answer_length, answer


def is_words_correct_type(data) -> bool:
    if not isinstance(data, list):
        return False

    for i in data:
        if not isinstance(i, str):
            return False

    return True
