# here we will learn about list
# list is mutable
# list have [] (brackets)
ingredients = ["Water" , "milk" , "black tea"]
ingredients.append("sugar")
print(f"Ingredients are : {ingredients}")
ingredients.sort()
print(ingredients) # sort it

# sort some numbers using list
numbers = [0,3,2,1]
numbers.sort()
print(numbers)

# try to add something
# extend
# insert functions
ingredients.insert(0,"Cardamom") # at 0th position we have inserted
print(ingredients)

last_element = ingredients.pop()
print(last_element)

#  find maximum and minimum number from it
temp_list = [34,36,23,12,50]
print(f"Highest temp is : {max(temp_list)}")

students = [
    ("Arnab",32),
    ("Raaz" , 36),
    ("Srijan" , 54)
]
print(students)

# list concatenation 
list_1 = ["Arnab" , "Valluk"]
list_2 = ["Misri" , "Sugar"]
list_3 = list_1 + list_2
print(list_3)

