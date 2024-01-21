def isAnagram_sol1(s, t):
    key_str1 = ''.join(sorted(s))
    print(key_str1)
    key_str2 = ''.join(sorted(t))
    print(key_str2)
    if key_str1 != key_str2:
        return False
    return True

def isAnagram_sol2(s, t):
    map = {}
    if len(s) != len(t):
        return False
    for i in range(0, len(s)):
        if s[i] not in map:
            map[s[i]] = 1
        else:
            map[s[i]] = map[s[i]] +1
    for i in range(0, len(t)):
        if t[i] not in map:
            return False
        else:
            map[t[i]] = map[t[i]] - 1
        if  map[t[i]] ==0:
            map.pop(t[i])

    if len(map) != 0:
        return False
    return True


def isAnagram(s, t):
    map = {}
    if len(s) != len(t):
        return False

    for i in range(0, len(s)):
        if s[i] not in map:
            map[s[i]] = 1
        else:
            map[s[i]] = map[s[i]] +1

    print(map)

    for i in range(0, len(t)):
        if t[i] not in map:
            return False
        else:
            map[t[i]] = map[t[i]] - 1
    print(map)
    for i in range(0, len(t)):
        if map[t[i]]!=0:
            return False
    return True


if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    # s = "ab"
    # t = "ba"
    # s = "aacc"
    # t = "ccac"
    # print(isAnagram(s, t))
    print(isAnagram_sol2(s,t))
