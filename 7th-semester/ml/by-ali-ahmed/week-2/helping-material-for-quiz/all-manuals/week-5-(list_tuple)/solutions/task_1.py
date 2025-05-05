n=eval(input("Enter The list:"))
'''l=[]
for i in n:
    if n.count(i)==1:
        l.append(i)
print(l)'''
new_list=[]
new_list=[i for i in n if n.count(i)==1]
print(new_list)
