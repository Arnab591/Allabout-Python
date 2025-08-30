# functions are block of code that perform a specefic task based on some sequential manner
# you are managing a busy tea stall and recieving many order
# want to print each customer name along with the type of chai they order
# this is a example of reduce code duplication
def print_order(name , chai_oder) :
    print(f"Thanks ! {name} and you have ordered :{chai_oder}")
customer = input("Enter your name sir :")
chai = input("What kind of chai you want to oder :")
print_order(customer , chai)

# here name and chai order are just placeholders



# splitting the complex task
