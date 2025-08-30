# crate a tuple of  five number and print each element
my_tuple = (1,2,4,3,5)
print(my_tuple)
length = len(my_tuple)
for i in my_tuple :
    print(i)
# access the last element of tuple 
print(my_tuple[length-1])

t = (10,30,40)
print(id(t))
temp = list(t)
temp.append(50)
t = tuple(temp)
print(id(t))
print(t)

# sort a tuple 
print(sorted(my_tuple))
print(my_tuple)

# find the minimum and maximum of tuple (5,2,9,1,7)
new_tuple = (5,2,9,1,7)
print(f"Maximum number from the tuple is :{max(new_tuple)}")
print(f"Minimum number from the tuple is :{min(new_tuple)}")

# count how many times 2 appears in the tuple (1,2,2,3,4,2,5)
newest_tuple = (1,2,2,3,4,2,5)
print(newest_tuple.count(2))

# concatenation
new1_tuple = (1,2)
new2_tuple = (3,4)
new3_tuple = new1_tuple + new2_tuple
print(new3_tuple)
