def solution(babbling):
    words = ["aya", "ye", "woo", "ma"]
    count = 0

    for i in range(len(babbling)):
        for word in words:
            if word in babbling[i] and not word*2 in babbling[i]:
                babbling[i] = babbling[i].replace(word, '*')
        if all(c == '*' for c in babbling[i]):
            count += 1

    return count