import collections       
def majorityElement(nums):
    dictionary = (collections.Counter(nums))
    filtered = filter(lambda item: item[1] > len(nums) / 3, dictionary.items())
    return map(lambda a: a[0], filtered)

print (majorityElement([3, 2, 3]))