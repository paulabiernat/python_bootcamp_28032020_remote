with open("emails.txt") as f:
    for line in f:
        line = line.lower()
        line = line.strip()
        print(line)

