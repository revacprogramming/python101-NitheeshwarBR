# Lists
# 8.4 Open the file romeo.txt and read it line by line. For each line,
#  split the line into a list of words using the split() method. The program should build a list of words. 
#  For each word on each line check to see if the word is already in the list and if not append it to the list. 
# When the program completes, sort and print the resulting words in alphabetical order.
def lists():
    filename = "dataset/romeo.txt"
    file=open(filename)
    lines=list()
    for line in file:
        words=line.split()
        [lines.append(i) for i in words if i not in lines] #line comprenhension       
    lines.sort()
    print(lines)
lists()


    	    


    
