def minFlips(a, b, c):
        binB = bin(b)[2:]
        binA = bin(a)[2:]
        binC = bin(c)[2:]
        maxLen = max(len(binA), len(binB), len(binC))
        # print(binA, binB, binC)

        while len(binA) < maxLen:
            binA = "0" + binA
        while len(binB) < maxLen:
            binB = "0" + binB
        while len(binC) < maxLen:
            binC = "0" + binC
        # print(binA, binB, binC)
        res = 0
        for i in range(len(binA)):
#           clear both A and B
            # import pdb;pdb.set_trace()
            if binC[i] == "0":
                if binA[i] == "1":
                    res += 1
                if binB[i] == "1":
                    res += 1
            elif binC[i] == "1":
                if binA[i] == "0" and binB[i] == "0":
                    res += 1
        return res
a=6
b=783
c=863 
#2
print(minFlips(a, b, c))

# (Pdb) binC
# '0b1101011111'
# (Pdb) binA
# '0b00000110'
# (Pdb) binB
# '0b1100001111'