def solve():
    n = int(input())
    strings = input().split()
    characters = dict()
    keys = []
    for i in range(26):
        characters[chr(i+97)] = set()
        keys.append(chr(i+97))
    for word in strings:
        characters[word[0]].add(word[1:])
    total_count = 0 
    for i in range(26):
        words1 = characters[chr(i+97)]
        for j in range(i+1,26):
            words2 = characters[chr(j+97)]
            for w1 in words1:
                for w2 in words2:
                    if w1 not in words2 and w2 not in words1:
                        total_count += 2 
    print(total_count)

    

if __name__ == '__main__':
    for t in range(int(input())):
        solve()