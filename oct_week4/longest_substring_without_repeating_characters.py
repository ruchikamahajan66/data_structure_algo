def longest_substring(str):
    new_set = set()
    l = 0
    res = 0
    for r in range(0, len(str)):
        while str[r] in new_set:   # "w"
            new_set.remove(str[l])      #"p"
            l = l+1        # 1
        new_set.add(str[r])   # "p" "w" , "p", "k", "e"
        size_of_window = r-l+1
        if size_of_window> res:
            res = size_of_window
    return res


if __name__ == '__main__':
    str = "pwwkew"
    print(longest_substring(str))
