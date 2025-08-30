# scoped and named spaces in python
def serve_chai():
    chai_type = "Masala" #local scope
    print(f"Inside Function {chai_type}")
chai_type = "Lemon"
serve_chai()
print(f"Outside function {chai_type}") #outer scope

# Scopes are --> Global scope , Local scope , Enclosing scope
# Local scopes are inside a function
def wild_life():
    wild_animal = "Elephant"
    print(f"The prominant animal is : {wild_animal}")
wild_animal = "Tiger"
print(f"Outer animal is : {wild_animal}")
wild_life()


