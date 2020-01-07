jobNames = []
srTitles = ['Senior', 'Manager', 'Sr', 'Lead', 'Staff', 'Director']
mobileTitles = ['Android', 'iOS', 'IOS','iOS', 'Mobile']
obscureTitles = ['Time', 'Electrical', 'DevOps', 'Network Reliability', 'Machine Learning', 'Come']

with open("square_positions.txt") as file: 
    for idx, line in enumerate(file):
        isSenior = False #no sr
        for srTitle in srTitles:
            if srTitle in line: isSenior = True

        isMobile = False #no mobile
        for mobileTitle in mobileTitles:
            if mobileTitle in line: isMobile = True

        isObscure = False #no obscure
        for obscureTitle in obscureTitles:
            if obscureTitle in line: isObscure = True
        if not isSenior and not isObscure and not isMobile and 'Engineer' in line: #contains 'Engineer'
            jobNames.append(line)
print("LISTINGS:")
jobNames = list(filter(lambda a: len(a.split()) < 10, jobNames)) # short titles
# jobNames.sort() 
jobNames = set(jobNames) #unique
for idx, jobName in enumerate(jobNames):
    print(idx+1)
    print(jobName)
quant = len(jobNames)
print("{}".format(quant))