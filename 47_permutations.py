import collections
def permuteUnique(nums):
    res = []
    def recurse(curr, counter):
        if len(curr) == len(nums):
            res.append(curr[::])
        for key in counter:
            if counter[key] > 0:
                counter[key] -= 1
                curr.append(key)
                recurse(curr, counter)
                curr.pop()
                counter[key] += 1
    recurse([], collections.Counter(nums))
    return res

    # works but not for Negatives
    # res = set()
    # def recurse(curr, idx):
    #     print(curr)
    #     if len(curr) == len(nums):
    #         res.add("".join([str(i) for i in curr]))
    #         return
    #     for i in range(idx, len(nums)):
    #         for pos in range(len(curr) + 1):
    #             recurse(curr[0:pos] + [nums[i]] + curr[pos:], i + 1)
    # recurse([], 0)
    # return list(res)

print(permuteUnique([1,1,2]))