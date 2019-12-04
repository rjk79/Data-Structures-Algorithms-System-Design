# 1 I

def intToRoman(num):
    res = ""
    # need to all special cases but not specific ones like 14 => handled by IV
    syms = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"][::-1]
    vals = [1,    4,    5,   9,    10, 40,   50,  90,  100, 400, 500, 900, 1000][::-1]
    idx = 0
    while num > 0:
        import pdb;pdb.set_trace()
        quant = num // vals[idx]
        res += quant * syms[idx]  
        num %= vals[idx]
        idx += 1
    return "".join(res)
print(intToRoman(3))