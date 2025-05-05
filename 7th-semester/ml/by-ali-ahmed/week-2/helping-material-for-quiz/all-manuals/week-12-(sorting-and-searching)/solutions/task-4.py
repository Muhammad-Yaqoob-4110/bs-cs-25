l=eval(input("Enter an unsorted list:"))
num=int(input("Enter a number you want to find:"))
for i in range(len(l)):
    if l[i]==num:
        print("The Required is in the",i+1,"place")
        exit()
else:
    print("The required number is not in the list.")