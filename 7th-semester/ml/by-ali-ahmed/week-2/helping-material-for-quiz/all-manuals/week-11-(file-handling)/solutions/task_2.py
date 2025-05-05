def st_lis(m):
    n = ""
    for i in range(len(m)):
        n += m[i]
    kl = n.strip()
    kl=kl.split()
    return (kl)
def eligibility(sc):
    if int(sc)<75:
        return "Eligible"
    else:
        return "Not Elligible"

def perce(n,m):
    h=(n/m)*(100)
    return h
print("Course: Fundamentals of Programming And Data Science")
while 1:
   s=input('''What do you want to do?
1) Enter a new Attendence
2) Eligibility''')
   if s=="1":
    fileop=open("Attendence record","r+")
    d = fileop.readlines()
    # print(d)
    fileop.write("\n")
    c = d[0:1]
    k = st_lis(c)
    l = ""
    for i in k:
        print(i, ":", end="")
        p = input()
        p = p.upper()
        l += (p)
        if k[k.index(i)] == 17:
            break
        l += (" ")
    fileop.close()
    print(l)
    filesp = open("Attendence record", "a+")
    filesp.write(l)
    filesp.close()
   elif s=="2":
    fileop = open("Attendence record", "r+")
    d = fileop.readlines()
    c2 = []
    for i in range(len(d)):
        c1 = st_lis(d[i])
        c2.append(c1)
    ccc = st_lis(d[0])
    for i in range(17):
        dd = ""
        sf, bf = 0, 0
        for j in range(2, len(c2)):
            dd += c2[j][i]
            dd += "   "
            if c2[j][i] == "P":
                sf += 1
            else:
                bf += 1
        v=perce(sf, len(c2) - 2)
        print(ccc[i], "  ", i + 1, "  ", dd, "  ", v," ",eligibility(v))
   hjj=input("Do you want to close the system? (y/n)")
   if hjj.lower()=="y":
    break
   else:
    continue
