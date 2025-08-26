# dictionary is a key order pair collections
chai_order = dict(type="Masala chai" , size = "Large" , sugar = 2)
print(chai_order)
print(chai_order["type"]) 
chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["Liquid"] = "milk"

# membership testing
print(f" Is sugar is in order : {'sugar' in chai_order}")

note = chai_recipe.get('billi' , 'no') # safe method of extracting
print(note)

# dictionary
my_dict = {"name" : "Arnab Chakraborty" , "class" : "HS" , "cgpa" : 6}
name = my_dict["name"]
print(name)

# update things in dictionary

# popitem
my_dict.update({"name" : "Rishi sunak"})
print(my_dict)
