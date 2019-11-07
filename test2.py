import collections
string = "GCTAGCGCTATATATAGCGCGCTATATCGC"

dic = {
    "A": "T",
    "T": "A",
    "C": "G",
    "G": "C"
}

print (collections.Counter(string).items())

b = "TAC"
print (b in string or reversed([dic[char] for char in list(b)]) in string)
# print (list(b))

# for i in range(len(string)):
#     for j in range(i, len(string)):
#         print(string[i:j])

