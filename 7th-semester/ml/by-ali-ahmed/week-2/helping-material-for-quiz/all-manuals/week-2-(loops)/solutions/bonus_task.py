def password(k):
    v = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    m = ("abcdefghijkmnopqrstuvwxyz")
    d = ("1234567890")
    s_p = ("@,><./?#~!$%^&*()_- \\")
    l = 0
    a = 0
    q = 0
    u = 0
    l_s=0
    if(len(k)) > 7:
       l_s=1
    for i in p:
        if i in v:
            l += 1
        elif i in m:
            a += 1
        elif i in d:
            q += 1
        else:
            u += 1


    if l == 0 or a == 0 or q == 0 or u == 0 or l_s==0:
        if l_s==0:
            print("The Legth of your password must be more than 7.")
        if l == 0:
            print("Your Password must contain An Upper_case Character.")
        if a == 0:
            print("Your Password must contain An Lower_case Character.")
        if q == 0:
            print("Your Password must contain An Digit.")
        if u == 0:
            print("Your Password must contain An Special Character.")
        return 1
    else:
        print("Your Suggested Password is strong.")
        return 0


while 1:
    p = input("Enter the Password:")
    s=password(p)
    if s==1:
        continue
    else:
        break
