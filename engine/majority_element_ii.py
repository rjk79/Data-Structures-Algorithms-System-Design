import collections
def majorityElement(nums):
    ctr = collections.Counter()
    for n in nums:
        import pdb;pdb.set_trace()
        ctr[n] += 1
        if len(ctr) == 3:
            ctr -= collections.Counter(set(ctr))
    return [n for n in ctr if nums.count(n) > len(nums)/3]
print(majorityElement([1, 1, 1, 2, 2, 3, 3, 3]))