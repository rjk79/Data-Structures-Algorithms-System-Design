def countBits(num):
    iniArr = [0]
    if num > 0:
        while len(iniArr) < num + 1:
            iniArr.extend([x+1 for x in iniArr])
            print(iniArr)
    return iniArr[0:num+1]

(countBits(6))