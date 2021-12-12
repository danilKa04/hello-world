with open(r"E:\test111.txt", "r") as file:

lines = file.readlines()

print(lines.index("мусор\n"))
