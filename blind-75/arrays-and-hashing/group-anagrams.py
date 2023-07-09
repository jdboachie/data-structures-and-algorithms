def group_anagrams(strs: list(str)) -> list[list[str]]:
    anagrams = {}

    for string in strs:
        count = [0] * 26

        for char in string:
            count[ord(char) - ord("a")] += 1

        if tuple(count) in anagrams:
            anagrams[tuple(count)].append(string)
        else:
            anagrams[tuple(count)] = [string]

    return anagrams.values()
