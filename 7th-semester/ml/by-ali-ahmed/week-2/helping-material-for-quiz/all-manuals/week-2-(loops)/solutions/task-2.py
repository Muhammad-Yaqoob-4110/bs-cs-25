P=("abcdefghijklmnopqrstuvwxyz")
user=input("Enter a Sentence:")
user=user.lower()
w=""
for i in range(len(user)):
    if user[i] in P:
       w+= user[i]
    else:
        continue

a=w.count("a")+w.count("e")+w.count("i")+w.count("o")+w.count("u")
c=len(w)-a
print(f'''Vowels: {a}
Consonants: {c}''')

