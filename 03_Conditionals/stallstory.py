# A tea stall offers different pricds for different cup sizes
# Write a program that calculates the price based on size
print("Enter which chai you want ?")
chai_order = input("1.small 2. medium 3.large :")
if(chai_order.lower() == "small"):
    print("Order confirmed small chai --> $10")
elif (chai_order.lower()== "medium"):
    print("Order confirmed ! medium chai --> &15")
elif(chai_order.lower()=="large"):
    print("Order confirmed ! large chai --> &20")
else : 
    print("Umknown cup size")