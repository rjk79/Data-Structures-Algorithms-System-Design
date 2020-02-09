def checkIfExist(arr):
    seen = dict()
    for idx, el in enumerate(arr):
        print(seen, el, idx)
        if el * 2 in seen and idx != seen[el*2]: #double has been found and it's at a different idx
            return True
        seen[el] = idx
    for idx, el in enumerate(arr):
        if el * 2 in seen and idx != seen[el*2]:
            return True
        seen[el] = idx
    
    return False   
arr = [10,2,5,3]

print(checkIfExist(arr))