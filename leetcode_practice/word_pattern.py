# pattern = "abba"
#  list = [dog, cat, cat, dog]
# map = {
#       a = dog
# }
def wordPattern(pattern, s):
    map1 = {}
    map2 = {}
    list = s.split(" ")
    if len(list) != len(pattern):
        return False
    for i in range(0, len(list)):
        if list[i] not in map1:
            if pattern[i] not in map2:
                map1[list[i]] = pattern[i]
                map2[pattern[i]] = list[i]
            else:
                return False
        else:
            if map1[list[i]] != pattern[i]:
                return False
    return True

def wordPattern_sol2(pattern, s):
    map1 = {}
    map2 = {}
    list = s.split(" ")
    if len(list) != len(pattern):
        return False
    for i in range(0, len(list)):
        if list[i] not in map1:
            if pattern[i] not in map2:
                map1[list[i]] = pattern[i]
                map2[pattern[i]] = list[i]
            else:
                return False
        else:
            if map1[list[i]] != pattern[i]:
                return False
    return True

if __name__ == '__main__':
    pattern = "abba"
    s = "dog cat cat dog"
    print(wordPattern_sol2(pattern, s))
