# Files
# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and
#  compute the average of those values and produce an output as shown below. 
# Do not use the sum() function or a variable named sum in your solution.
filename = "dataset/mbox-short.txt"
file=open(filename)
count=0
add=0
for line in file:
    if line.startswith('X-DSPAM-Confidence:'):
        count=count+1
        # num=line.find("0")
        # t=line[num:]
        # add=add+float(t)
        words=line.split()
        num=words[1]
        add=add+float(num)
average=add/count
print("Average spam confidence:",average)
