import random
valid_characters=""
length=int(input("Enter the Length of the password="))
upper=input("Do you want to Enter Upper Case Characters? (Y/N)")
if upper=="Y":
    valid_characters+=("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
else:
    valid_characters
lower=input("Do you want to Enter Lower Case Characters? (Y/N)")
if lower=="Y":
    valid_characters+=("abcdefghijklmnopqrstuvwxyz")
else:
    valid_characters
digits=input("Do you want to Enter Digits? (Y/N)")
if digits=="Y":
    valid_characters+=("1234567890")
else:
    valid_characters
spe_char=input("Do you want to Enter Special Characters? (Y/N)")
if spe_char=="Y":
    valid_characters+=("\@!*^%$#()&_:;?/~")
else:
    valid_characters
i=0
r=""
while i<length:
    r+=random.choice(valid_characters)
    i+=1
print(r)



