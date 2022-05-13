# Dictionaries
filename = "dataset/mbox-short.txt"
handle = open(filename)

lines = list()

for line in handle:
    if not line.startswith("From:"): continue
    line = line.split()
    lines.append(line[1])

counts = dict()
for word in lines:
    counts[word] = counts.get(word,0) + 1

x = 0
y = 0
for word,count in counts.items(): 
    if x ==0 or count > x:
        x = count
        y = word

print (y,x)

