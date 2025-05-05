byte=int(input("Enter Bytes:"))
p=input('''What you want to get:
Press 1 for MegaBytes
Press 2 for GigaBytes
=''')
if p=="1":
    c=byte/(1024*1024)
    print("%.2f Bytes are equal to %.2e MegaBytes."%(byte,c))
elif p=="2":
    d=byte/(1024*1024*1024)
    print("%.2f Bytes are equal to %.2e GigaBytes."%(byte,d))
else:
    print('''You Entered an invalid Number.
Rerun the code and please enter Valid Character!!!''')
