def beforeAndAfterPuzzles(phrases):
        res = []
        for i1, phrase1 in enumerate(phrases):
            for i2, phrase2 in enumerate(phrases):
                if i1 != i2:
                    if phrase1.split(" ")[-1] == phrase2.split(" ")[0]:
                        joint = phrase1 + " " + " ".join(phrase2.split(" ")[1:] ) #take 1st word off 2nd phrase
                        res.append(joint.strip(" "))
        res = list(set(res))
        res.sort()
        return res

a = ["writing code","code rocks"]
print(beforeAndAfterPuzzles(a))