def evalRPN(tokens):
    #form a stack
    #whenever we hit an operATOR, we remove top 2 els from stack
    stack = []
    res = None
    operators = ['+', '-', '*', '/']
    for el in tokens:
        if el not in operators:
            stack.append(int(el))
        else:
            curr = stack.pop()
            if res is None:
                prev = stack.pop()
            else:
                prev = res
            
            if el == '+':
                res = prev + curr
            elif el == '-':
                res = prev - curr
            elif el == '*':
                res = prev * curr
            elif el == '/':
                res = prev // curr
    return res

tokens = ["2","1","+","3","*"]
print(evalRPN(tokens))

print(5/ 2)
print(5// -2)