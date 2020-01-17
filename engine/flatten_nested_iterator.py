def flatten(arr):
    res = []
    for el in arr:
        if isinstance(el, list):
            res.extend(flatten(el)) #ret 1d arr
        else:
            res.append(el)
    return res
print(flatten([[1, 2, 3], 
                [4, 5, 6, 
                    [7, 8]
                ]
            ]))