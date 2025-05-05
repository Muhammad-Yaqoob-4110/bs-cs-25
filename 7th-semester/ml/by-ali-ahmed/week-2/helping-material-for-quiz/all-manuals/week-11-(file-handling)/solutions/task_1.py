fileptr = open("input.txt", "w+")
for i in range(5):
    p=input("Enter a line:")
    fileptr.write(p)
    fileptr.write("\n")
fileptr.close()
fileptr = open("input.txt", "r")
if fileptr:
 print("file is opened successfully")
for i in range(5):
   string=(fileptr.readline())
   filept=open("output.txt","a")
   words = string.split()
   for word in words:
    word=word[::-1]
    filept.write(word)
    filept.write(" ")
   filept.write("\n")
fileptr.close()