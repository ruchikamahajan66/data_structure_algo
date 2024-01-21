def isIsomorphic(s, t):
    map1 = {}
    map2 = {}
    if len(s) != len(t):
        return False
    for i in range(0, len(s)):
        if s[i] not in map1:
            if t[i] not in map2:
                map1[s[i]] = t[i]
                map2[t[i]] = s[i]
            else:
                return False
        else:
            if map1[s[i]] != t[i]:
                return False
    return True


if __name__ == '__main__':
    s = "badc"
    t = "baba"
    print(isIsomorphic(s, t))

