with open("inputs/day01.txt", "r") as fh:
    contents = fh.readlines()

max_cals = 0
cals = 0
for line in contents:
    if line.strip() == "":
        max_cals = max(cals, max_cals)
        cals = 0
    else:
        cals += int(line.strip())

max_cals = max(cals, max_cals)

print(max_cals)

