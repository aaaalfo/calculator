import re

precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

st = input()
string = ''
for s in st:
    if s != " ":
        string += s

divided_string = [d for d in re.sub(r'([-+*/^()])', r' \1 ', string).split() if d]

for d in range(len(divided_string)):
    if divided_string[d].isdigit():
        divided_string[d] = int(divided_string[d])



outpt = []
stack = []


for d in divided_string:
    if isinstance(d, int):
        outpt.append(d)
    elif d == '(':
        stack.append(d)
    elif d == ')':
        while stack and stack[-1] != '(':
            outpt.append(stack.pop())
        stack.pop()
    else:
        while (stack and stack[-1] != '(' and precedence[stack[-1]] >= precedence[d]):
                outpt.append(stack.pop())
        stack.append(d)
outpt.extend(reversed(stack))

for i in range(len(outpt)):
    for j in range(len(outpt)):
        if outpt[j] == '+':
            outpt[j] = outpt[j - 2] + outpt[j - 1]
            del outpt[j - 1]
            del outpt[j - 2]
            break
        elif outpt[j] == '-':
            outpt[j] = outpt[j - 2] - outpt[j - 1]
            del outpt[j - 1]
            del outpt[j - 2]
            break
        elif outpt[j] == '*':
            outpt[j] = outpt[j - 2] * outpt[j - 1]
            del outpt[j - 1]
            del outpt[j - 2]
            break
        elif outpt[j] == '/':
            outpt[j] = outpt[j - 2] / outpt[j - 1]
            del outpt[j - 1]
            del outpt[j - 2]
            break
        elif outpt[j] == '^':
            outpt[j] = outpt[j - 2] ** outpt[j - 1]
            del outpt[j - 1]
            del outpt[j - 2]
            break
print(outpt[0])