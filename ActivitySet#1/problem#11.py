# Tuples
# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by 
# hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding 
# the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
filename = "dataset/mbox-short.txt"
handle = open(filename)

lines=list()
for line in handle:
    if line.startswith("From:"):
        continue
    elif line.startswith("From"):
        words=line.split()
        words=lines.append(words[5])
    elif not line.startswith("From"):
        continue
        
x=list()
for letters in lines:
    letter=letters.split(':')
    letter=x.append(letter[0])
x.sort()
hours=dict()
for hrs in x:
    if hrs not in hours:
        hours[hrs]=1
    else:
        hours[hrs]+=1
result=hours.items()

for hr,c in result:
    print(hr,c)