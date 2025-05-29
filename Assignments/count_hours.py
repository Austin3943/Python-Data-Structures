name = input("enter file: ")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = {}
for line in handle:
    if not line.startswith("From "):
        continue
    words = line.split()
    time = words[5]
    hour = time.split(":")[0]
    counts[hour] = counts.get(hour, 0) + 1

handle.close()

for hour in sorted(counts):
    print(hour, counts[hour])
