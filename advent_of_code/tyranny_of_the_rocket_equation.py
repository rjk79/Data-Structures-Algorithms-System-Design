
lines = open("./tyranny_of_the_rocket_equation.txt").read().splitlines()
# Question 1:
# res = 0
# for num in lines:
#     res += (int(num) // 3 - 2)
# print(res)

def recurse(mass):
    if mass == 0: 
        return 0
    newMass = mass // 3 - 2
    if newMass < 0: newMass = 0
    return newMass + recurse(newMass)


# Question 2:
res = 0
for num in lines:
    res += recurse(int(num))
print(res)

# print(recurse(14)) #2
# print(recurse(1969)) #966
# print(recurse(100756)) #50346

