# we are making a kettle notification system
# where if kettle water is boiled we will give notification to the uer
kettle_boiiled = input("Enter True or False :")
if kettle_boiiled.lower() == "true":
    bool_kettle = True
else:
    bool_kettle = False
if(bool_kettle==True):
    print("Kettle done ! Time to make the chai")
else:
    print("Make it properly hot")