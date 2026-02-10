users = {}

file = open("Login.csv", "r")
lines = file.readlines()
file.close()

for i in range(1, len(lines)):
    data = lines[i].strip().split(",")
    users[data[0]] = {
        "password": data[1],
        "status": data[2]
    }

print("User Dictionary:")
print(users)

name = input("Enter username: ")
pwd = input("Enter password: ")

try:
    if users[name]["password"] == pwd:
        if users[name]["status"] == "1":
            print(name.lower(), "is loggined")
        else:
            print(name.lower(), "is not loggined")
    else:
        print("Wrong password")

except KeyError:
    print("Username not found")
