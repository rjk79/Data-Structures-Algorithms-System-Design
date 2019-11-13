def evalRPN(tokens):
        
    operators = ["*", "/", "+", "-"]
    stack = []
    for token in tokens:
        if token not in operators:
            stack.append(int(token))
        else:
            r, l = stack.pop(), stack.pop()
            if token == "*":
                stack.append(r * l)
            elif token == "+":
                stack.append(r + l)
            elif token == "-":
                stack.append(l - r)
            elif token == "/":
#                   1/-22
                if l * r < 0 and l % r != 0:
                    import pdb; pdb.set_trace()
                    print(l, r, l/r + 1)
                    stack.append(l / r + 1)
                else:
                    stack.append(l / r)
    return stack.pop()
print(evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))