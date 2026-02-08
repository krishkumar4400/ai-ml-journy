# Match Case:

color = input("Enter color: ")

match color:
    case "green":
        print("Go")
    case "yello":
        print("Look")
    case "red":
        print("Stop")
    case _:
        print("Wrong Color !")