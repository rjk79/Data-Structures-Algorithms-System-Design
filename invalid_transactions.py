import collections

def invalidTransactions2(transactions):
        class Transaction:
            def __init__(self, person, time, amount, city):
                self.person = person
                self.time = int(time)
                self.amount = int(amount)
                self.city = city
        transacts = []
        for transaction in transactions:
            transacts.append(Transaction(*transaction.split(","))) #unpack
        transacts.sort(key = lambda a: a.time)
        dic = collections.defaultdict(list)
        for idx, transact in enumerate(transacts):
            dic[transact.person].append(idx)
        res = []
       
        for idx in range(len(transacts)):
            # import pdb;pdb.set_trace()
            curr = transacts[idx]
            if curr.amount > 1000:
                res.append("{},{},{},{}".format(curr.person, curr.time, curr.amount, curr.city)) #interpolate
            
            for idx2 in range(idx+1, len(transacts)):
                curr2 = transacts[idx2]
                if curr.person == curr2.person and curr2.time <= curr.time + 60 and curr.city != curr2.city: 
                    res.append("{},{},{},{}".format(curr.person, curr.time, curr.amount, curr.city)) #interpolate
                    res.append("{},{},{},{}".format(curr2.person, curr2.time, curr2.amount, curr2.city)) #interpolate

        return set(res)
# print(invalidTransactions1(["alice,10,800,mtv","alice,30,100,beijing", "alice,60,100,giza", "alice,80,100,nyc"]))
# print(invalidTransactions2(["alice,10,800,mtv","alice,30,100,beijing", "alice,60,100,giza", "alice,80,100,nyc"]))

# print(invalidTransactions1(["alice,20,800,mtv","bob,50,1200,mtv"])) #doesnt care about time of 1st one since 2nd one is invalidated by amount
print(invalidTransactions2(["alice,20,800,mtv","bob,50,1200,mtv"])) #doesnt care about time of 1st one since 2nd one is invalidated by amount
print(invalidTransactions2(["alice,20,800,mtv","alice,50,100,beijing"])) #doesnt care about time of 1st one since 2nd one is invalidated by amount

# 1. make class
# 2. make them all instances of that class
# 3. sort by time
# 4. map each person to their transactions
# 5. compare every transaction to every other, checking all 4 conditions (amount, name, time, city)