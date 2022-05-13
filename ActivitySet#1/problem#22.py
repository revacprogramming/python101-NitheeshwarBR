file=open('mbox-short.txt')
lines=list()
count=0
for line in file:
    if line.startswith('From:'):
        continue
    elif line.startswith('From'):
        count=count+1
        lines=line.split()
        words=lines[1]
        print(words)
        
            
print("There were {} lines in the file with From as the first word".format(count))