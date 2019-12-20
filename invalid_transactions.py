import collections
def invalidTransactions1(transactions):
    class Transaction:
        def __init__(self, name, time, amount, city):
            self.name = name
            self.time = int(time)
            self.amount = int(amount)
            self.city = city

    res = set()
    transactions = [Transaction(*t.split(',')) for t in transactions] # O(n) time
    transactions.sort(key=lambda t: t.time) # O(nlogn) time

    for i in range(len(transactions)): # O(n^2) time
        t1 = transactions[i]
        if t1.amount > 1000:
            res.add("{},{},{},{}".format(t1.name, t1.time, t1.amount, t1.city))
        for j in range(i+1, len(transactions)):
            # import pdb;pdb.set_trace()
            t2 = transactions[j]
            # diff less than 60
            if t2.name == t1.name and t2.time-t1.time <= 60 and t2.city != t1.city:
                res.add("{},{},{},{}".format(t1.name, t1.time, t1.amount, t1.city))
                res.add("{},{},{},{}".format(t2.name, t2.time, t2.amount, t2.city))
    
    res = list(res) # O(n) time
    return res


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