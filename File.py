file = open("sample.csv", "r")
lines = file.readlines()
for line in lines[1:]:
    name, salary,capable = line.strip().split(",")
    person = {"name": name, "salary": salary, "capable": capable}
    print(person)
file.close()