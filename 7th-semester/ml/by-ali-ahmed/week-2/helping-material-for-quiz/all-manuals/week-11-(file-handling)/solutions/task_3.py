def st_lis(m):
    n = ""
    for i in range(len(m)):
        n += m[i]
    kl = n.strip()
    kl = kl.split()
    return (kl)
def list_st(a):
    st=""
    for i in a:
        st+=i
        st+=" "
    return st
c2=[]
fileopt=open("stock.txt","r+")
d=fileopt.readlines()
for i in d:
    c1=st_lis(i)
    c2.append(c1)
fileopt.close()
prin="\033[1m"+"PRICES"+"\033[0m"
print("\033[1m"+"ITEMS"+"\033[0m",prin.center(40))
km=0
for i in c2[0]:
    mk=str(c2[1][km])
    print(i,mk.center(30))
    km+=1
bill = 0
ds = []
kgkg=[]
while 1:
    k = input("Name:")
    k=k.capitalize()
    if k in c2[0]:
        cc=c2[0].index(k)
        p = int(input("Enter the quantity"))
        c = (int(c2[1][cc])) - p
        c=str(c)
        list_=[k,c,c2[2][cc]]
        kgkg.append(p)
        (c2[1][cc]) = c
        fileopt = open("stock.txt", "w+")
        for i in c2:
            fileopt.write(list_st(i))
            fileopt.write("\n")
        fileopt.close()
        ds.append(list_)
    else:
        print("The required item is not available in our store.")
    pl=input("Do You want to buy more items? (y/n)")
    pl=pl.lower()
    if pl=="y":
        continue
    else:
        break
print(kgkg)
#Main thing of the program
print("\n \n \n \n")
lkk='BHAI BHAI'
lpk="\033[1m"+lkk+"\033[0m"
print(lpk.center(70))
addd="Address: Moon Market Lahore, Punjab 54000"
print(addd.center(65))
tele="Tele: 011223344"
print(tele.center(62))
print("* "*34)
cc="CASH RECEIPT"
print(cc.center(62))
print("* "*34)
kls="DESCRIPTION";quant="QUANTITY";price="TOTAL PRICE"
lpk="\033[1m"+kls+"\033[0m";dfk="\033[1m"+quant+"\033[0m";lpl="\033[1m"+price+"\033[0m"
print(lpk,dfk.center(40),lpl.center(41))
m=0
for i in ds:
    tht=str(i[0])
    knk=str(int(i[2])*kgkg[m])
    lal=str(kgkg[m])
    m+=1
    print(tht,lal.center(43),knk.center(25))
    ik=int(i[2])
    bill=bill+int(knk)
print("* "*34)
yot="\033[1m"+"TOTAL"+"\033[0m";bil="\033[1m"+str(bill)+"\033[0m"
print(yot.center(60),bil.center(30))
print("* "*34)
plk="\033[1m"+"THANKYOU"+"\033[0m"
print(plk.center(70))