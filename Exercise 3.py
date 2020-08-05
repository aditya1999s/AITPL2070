# Program to check positive number in list without ussing if-else, while


li = []
n = input("enter length : ")
for i in range(1, int(n)):
    k = int(input("enter value : "))
    li.append(k)
# we can also print positive no's using lambda exp.
pos_nos = list(filter(lambda x: (x > 0), li))

print("Positive numbers in the list: ", *pos_nos)