import time
def marks_calculation(c,wr,skip):
    time.sleep(1)
    print("Your Test is submitted successfully.")
    time.sleep(1)
    print("Wiat for few Seconds...")
    time.sleep(2)
    print("Correct Answers:", (c), "Skipped Questions:", (skip), "Wrong Answers:", wr)
    print("Your Result is:", ((c * 4) - wr))
    e=((c * 4) - wr)*(100/40)
    if e>=33:
        print("You are Eligible to Apply for Addmission.🥳🥳🤩😊")
    elif e<33:
        print("You are not Eligible to Apply for Addmission 😔☹️☹️")

# these are the mcqs for iteration in loops of ecat test
p_1_mcqs=("One light year is equal to:","A) 9 x 10^12m","B) 6 x 10^12","C)9.5 x 10^13m","D) None","F) skip","f","c","E) Submit","e")
p_2_mcqs=(" Reverse process of vector addition?","A) Subtraction","B) Division","C)Multiplication","D) None","F) skip","f","d","E) Submit","e")
p_3_mcqs=(" When a ball moves from and reaches to its maximum height in 3 seconds, what is its initial velocity?","A) 40m/sec","B) 29.4m/sec","C) 35m/sec","D) 25m/sec","F) skip","f","b","E) Submit","e")
p_4_mcqs=(" Rocket propulsion is according to?","A) 3rd law of motion","B) 2nd Law","C) 1st Law","D) None","F) skip","f","a","E) Submit","e")
p_5_mcqs=(" if the radius of circle is doubled, then centripetal force becomes:","A) Doubled"," B)Remains same","C) Half","D) Reduces Four times","F) skip","f","c","E) Submit","e")
p_6_mcqs=(" Bernoulli equation is according to ___________ law.","A) Stock’s law", "B) Einstiens equation","C)Newton’s law","D) None","F) skip","f","c","E) Submit","e")
p_7_mcqs=(" The time period of a second pendulum from its extreme to mean position:","A) T", "B) T/4","C) T/2","D) 2 sec","F) skip","f","d","E) Submit","e")
p_8_mcqs=(" At what temp, the velocity of sound is doubled than as that of at 100c:","A)859oC", "B) 560oC","C) 760oC","D) 500oC","F) skip","f","a","E) Submit","e")
p_9_mcqs=(" The range of visible wavelength spectrum is:","A) 400-750", "B) 100-400","C) 400-1000","D)300-600","F) skip","f","a","E) Submit","e")
p_10_mcqs=(" The range of wave no. of light is 5 x 106m-1. Then its wavelength is:","A) 2 x 107m", "B) 2 x 10-7 m","C) 5 x 10-8m","D) N one","F) skip","f","d","E) Submit","e")

# the list in which all the mcqs are stored
MCQs=(p_1_mcqs,p_2_mcqs,p_3_mcqs,p_4_mcqs,p_5_mcqs,p_6_mcqs,p_7_mcqs,p_8_mcqs,p_9_mcqs,p_10_mcqs)

# The code which displays the mcqs and calculates the numbers in case of submission
i=1; u=0; sk=0; ski=0; w=0; l=[]; j=1
print("Chose the correct option and write it's associated alphabet. Choose e to submit test and f to skip the mcqs.")
while i<=10:
    tup=MCQs[i-1]
    print(tup[0]); print(tup[1],"\t \t ",tup[2],"\n",tup[3],"\t \t ",tup[4],"\n",tup[8],"\t  \t \t",tup[5],sep="")
    p=input("Answer:")
    i += 1
    if tup[7]==p.lower():
        u+=1
    elif p.lower()==tup[6]:
        ski+=1; l+=tup; continue
    elif p.lower()==tup[9]:
        if i==2:
            ski =10
            marks_calculation(u,w,ski)
            exit()
        else:
            ski = ski + (12 - i)
            marks_calculation(u,w,ski)
            exit()
    else:
        w += 1
# the code which shows the skipped questions if NO. of skipped question(s) is >= 1
if ski >=1:
    lao = input("Enter 1 to attempt the skipped questions or 2 for Submission.")
    if lao=="1":
        while j<=ski:
            print(l[(10 * (j - 1)) + 0]);
            print(l[(10 * (j - 1)) + 1], "\t \t ", l[(10 * (j - 1)) + 2], "\n", l[(10 * (j - 1)) + 3], "\t \t ",l[(10 * (j - 1)) + 4], "\n", l[(10 * (j - 1)) + 8], "\t  \t \t", l[(10 * (j - 1)) + 5], sep="")
            p = input("Answer:")
            if l[(10 * (j - 1)) + 7] == p.lower():
                u += 1
            elif p.lower() == l[(10 * (j - 1)) + 6]:
                sk += 1
            elif p.lower() == l[(10 * (j - 1)) + 9] or "e":
                if j==1:
                    sk =ski
                    marks_calculation(u,w,sk)
                    exit()
                else:
                    sk=sk+ (ski - j+1)
                    marks_calculation(u,w,sk)
                    exit()
            else:
                w += 1
            j+=1
    elif lao=="2":
        marks_calculation(u,w,ski)
        exit()
marks_calculation(u,w,sk)
