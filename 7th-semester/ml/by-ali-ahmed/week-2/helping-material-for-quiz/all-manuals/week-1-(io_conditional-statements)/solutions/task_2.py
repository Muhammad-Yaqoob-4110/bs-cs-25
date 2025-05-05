ecat=int(input("Enter your ECAT Numbers:"))
inter=int(input("Enter your Intermediate (Part-1) Numbers:"))
p = input('''Enter your type of intermediate
Press 1 for ICS
Press 2 for F.Sc.(Medical)
Press 3 for F.Sc.(Engineering)
=''')
if p == "1":
    inter = (inter / 510) * 50
elif p == "2":
    inter = (inter / 505) * 50
elif p == "3":
    inter = (inter / 520) * 50
else:
    print('''You Entered the invalid Character😝😝😝
EXECUTION STOPPED!!!
Rerun the program''')
    exit()
matric = int(input("Enter your Matric Numbers:"))
matric=(matric/1100)*17
ecat=(ecat/400)*33
print("Your Aggregate is=",matric+inter+ecat)