def beforeAndAfterPuzzles(phrases):
    res = []
    for i, phrase1 in enumerate(phrases):
        for phrase2 in phrases[i+1:]:

            if phrase1.split(" ")[-1] == phrase2.split(" ")[0]:
                res.append(phrase1 + " " + " ".join(phrase2.split(" ")[1:] ) )
    return res

a = ["writing code","code rocks"]
print(beforeAndAfterPuzzles(a))