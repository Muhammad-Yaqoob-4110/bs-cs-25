def intersection():
    tup_1 = eval(input("Enter the first tuple:"))
    tup_2 = eval(input("Enter the second tuple:"))
    l = []
    tup = ()
    for i in tup_1:
        for j in tup_2:
            if i == j and i not in l:
                l.append(i)
    return l
print(intersection())

