def canConstruct(ransomNote, magazine):
    map = {}
    for i in range(0, len(magazine)):
        if not magazine[i] in map:
            map[magazine[i]] = 1
        else:
            map[magazine[i]] = map[magazine[i]] + 1

    for i in range(0, len(ransomNote)):
        if ransomNote[i] in map:
            map[ransomNote[i]] = map[ransomNote[i]] - 1
        else:
            return False
        if map[ransomNote[i]] == 0:
            map.pop(ransomNote[i])
    return True


if __name__ == '__main__':
    ransomNote = "aab"
    magazine = "abaa"
    print(canConstruct(ransomNote, magazine))
