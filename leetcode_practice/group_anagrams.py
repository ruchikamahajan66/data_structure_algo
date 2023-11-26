from collections import defaultdict

# ["eat","tea","tan","ate","nat","bat"]
#   ^
#   keyStr = sorted(s[i])
#   "aet"
#   "ant"
#
#
# {
# 	"aet" :["eat","tea","ate"],
# 	"ant": ["tan","nat"],
# 	"abt": ["bat"]
# }

def sol1(strs):
    map = {}
    res = []
    for word in strs:
        key_str = ''.join(sorted(word))
        if key_str not in map:
            map[key_str] = [word]
        else:
            map[key_str].append(word)
    for item in map.values():
        res.append(item)
    if res == []:
        res.append([])

    return res


def sol2(strs):
    anagram_map = defaultdict(list)

    for word in strs:
        sorted_word = ''.join(sorted(word))
        anagram_map[sorted_word].append(word)

    return list(anagram_map.values())


if __name__ == '__main__':
    # strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    strs = []
    print(sol1(strs))
    print(sol2(strs))

