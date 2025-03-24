import re
with open("log.txt") as file:
    for line in file:
        if re.search("ERROR", line):
            print(line)