icecream_flavour = ("Chocolate" , "Vanilla" , "Cherry")
(cream1 , cream2 , cream3) = icecream_flavour
icecream_flavour = icecream_flavour + ("Fruits",)
print(icecream_flavour)
print(f"My favourite ice cream is : {cream1}")

# check if element present in tuple 
# membership testing
print(f"IS Chocolate in ice cream ? {'Chocolate' in icecream_flavour}")
