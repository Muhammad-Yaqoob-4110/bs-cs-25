row_1=eval(input("Enter First row:"))
row_2=eval(input("Enter Second row:"))
row_3=eval(input("Enter Third row:"))
A=[row_1,row_2,row_3]
print("\nThe 3x3 matrix is:")
for i in range(0,3):
 for j in range(0,3):
   print(A[i][j]," ",end="")
 print("")
print("\nThe transpose of the matrix is:")
for i in range(0,3):
 for j in range(0,3):
   print(A[j][i]," ",end="")
 print("")