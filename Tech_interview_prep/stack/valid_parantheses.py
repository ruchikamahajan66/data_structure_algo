'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
'''

'''
Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''

def Isvalid_parantheses(s):
    st = []
    for c in s:
        if c in '{[(':
            st.append(c)
        elif c in ')]}':
            if not st or (c ==')' and st [-1]!= '(') or   (c =='}' and st [-1]!= '{') or  (c ==']' and st [-1]!= '['):
                print(False)
                break
            st.pop()
    else:
        print(True if not st else False ) #balanced if stack is empty


if __name__ == '__main__':
    string =  "{[()()]}"
    Isvalid_parantheses(string)
