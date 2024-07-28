file = open("company-names.txt", "r")
names = file.readlines()
count = 0
for name in names:
    print(name, end="")
    count+=1
    if(count == 1):
        break

file.close()