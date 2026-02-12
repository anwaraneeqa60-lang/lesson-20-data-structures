def match_words(word):
    ctr = 0
    lst = []
    for word in word:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)
    print("list of the words with first and last character same\n ", lst)
    return ctr
count = match_words(['abc', 'cfc', 'xyz', 'aba', '1221'])
print("numbers of words having first and last character same\n", count)