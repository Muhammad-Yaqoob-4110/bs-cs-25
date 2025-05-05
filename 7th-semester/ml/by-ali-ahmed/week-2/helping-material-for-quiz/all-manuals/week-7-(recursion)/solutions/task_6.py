def string_checker(n,a=0):
    s = []
    if a==len(n):
        return s
    else:
        c=n[a]
        if type(c)== str:
            s.append(n[a])
    a=a+1
    s.extend( string_checker(n,a))
    return s
p=[1,2,"Javaria",(1,3,4,5),{"a":"f","r":"i"},"Ahmad",("name",1,4),{2,3},"Kamran"]
print("The string elements in list are:",string_checker(p))