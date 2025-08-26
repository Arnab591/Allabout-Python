# match - case type property
# you make a ticket
seat_type = input("Enter your seat type (sleeper/Ac/general/luxury)").lower()
match seat_type:
    case "sleeper":
        print("Sleeper - No AC , beds available")
    case "ac":
        print("Ac three tier and 2 tier are available")
    case "general":
        print("Only seats are available ! No bed system")
    case "luxury" :
        print("Super delux bed with Ac ! Personal cabin")