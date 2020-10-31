# Adjacent Element Product
# Lets Suppose
#         0  1  2  3  4
# mylist = [1, 2, 3, 4, 5]
# Expected Output - 5*4 = 20
# we have to iterate till 4

mylist = list(map(int, input().split(",")))
print(mylist)
sum = []

for i in range(len(mylist)-1):  # range is 4 i.e. 0 1 2 3
    sum.append(mylist[i]*mylist[i+1])
largest_element = max(sum)
print(largest_element)
