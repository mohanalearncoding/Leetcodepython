#import priority as priority


def isAlienSorted( words, order):
    return words == sorted(words, key=lambda word: [order.index(c) for c in word])
    return words==words.sort(key= lambda x: [order.index(x[i]) for i in range(len(x))])
    print(words)
print(isAlienSorted(["hello","leetcode"],
"hlabcdefgijkmnopqrstuvwxyz"))