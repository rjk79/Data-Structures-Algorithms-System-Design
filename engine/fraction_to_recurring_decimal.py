def fractionToDecimal(numerator, denominator):
    n, remainder = divmod(abs(numerator), abs(denominator))
    sign = '-' if numerator*denominator < 0 else ''
    result = [sign+str(n), '.']
    stack = []
    while remainder not in stack:
        stack.append(remainder)
        n, remainder = divmod(remainder*10, abs(denominator))
        result.append(str(n))
    idx = stack.index(remainder)
    import pdb;pdb.set_trace()
    result.insert(idx+2, '(')
    result.append(')')
    return ''.join(result).replace('(0)', '').rstrip('.')

a = 1
b = 2
print(fractionToDecimal(a, b))
