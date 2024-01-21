def path(s):
    str = ""
    stack = []
    for i in range(0, len(s)):
        if s[i] == '/':
            if not s[i]:
                if s[i] == '..':
                    if not stack:
                        stack.pop()
                elif not s[i] == ".":
                    str.push(str)
            str = ""
        else:
            str = str + s[i]


if __name__ == '__main__':
    s = "/home//foo/.././././"
    path(s)
