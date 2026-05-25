# -*- coding: utf-8 -*-

import numpy as np
print ('\n'+"The input for the problem Ax = b is required in this manner. First the coefficient vector, x, will be asked. It will linear with some dimensions equal to the no of elemets. First enter the total number of elements of x. Then as prompted enter the every element of x one after the other as instructed. Press ENTER everytime to enter an element:-")
xlen = input(print('\n'+"Enter the number of elements for vector x:"))
print('\n')
xlen = int(xlen)
x = np.zeros(xlen)

for i in range(xlen):
    usrinp = input(print("Enter the number at position " + str(i)+":"))
    x[i] = float(usrinp);
print(x)
print('\n'+"Do the similar thing for matrix A as well and now enter the number of rows and columns when instructed")

while 1: #DIMENSIONALITY CHECK
   Arow = input(print('\n'+"Enter the number of rows for matrix A:"))
   Arow = int(Arow)
   Acol = input(print('\n'+"Enter the number of columns for matrix A:"))
   Acol = int(Acol)
   if Acol == xlen:
           print('\n'+"The dimensions of matrix A are consistent with the dimension of vector b. You can proceed.")
           break
   else:
           print("The number of columns of A are not same as the number of rows of b. Matrix multiplication NOT POSSIBLE. Kindly re-enter your inputs")
print('\n')

A = np.zeros((Arow,Acol))
for i in range(Arow):
    for j in range(Acol):
        usrinp = input(print("Enter the number at position " + str(i) + "," + str(j) + ":"))
        A[i][j] = float(usrinp)
print(A)

#INNER PRODUCT

print('\n'+"Printing the row vectors of A: -")

for i in range(Arow):
    print('Row No '+ str(i))
    print(A[i])
    print('\n')

I = np.zeros(Arow)
print('\n' + 'Inner Product')

for i in range(Arow):
    for j in range(Acol):
        I[i]+=A[i][j]*x[j]
    
print (I)

#OUTER PRODUCT

print('\n'+"Printing the column vectors of A: -")

for j in range(Acol):
    temp = np.zeros(Arow)
    print('Column No '+ str(j))
    for i in range(Arow):
        temp[i] = A[i][j]
    print(temp)
    print('\n')
    

O = np.zeros(Arow)
print('\n' + 'Outer Product')

for j in range(Acol):
    for i in range(Arow):
        O[i]+=A[i][j]*x[j]
    
print (O)

#COMPARING INNER AND OUTER PRODUCTS
print('\n' + "Comparing inner and outer products")
for i in range(Arow):
    print('\n' + 'At position ' + str(i) +':')
    print('\n' + "Outer Product Element:")
    print(O[i])
    print('\n' + "Inner Product Element:")
    print(I[i])
    print('\n' + "Difference between IP and OP Element At position " + str(i) +':')
    print(O[i]-I[i])
    if O[i] == I[i]:
        print('\n' + "Elements at position "+ str(i) +' are same')
        if i==Arow-1:
            print ('\n' + '\n' + "Inner and Outer Products have yielded the same results." + '\n')
            print(O)
    else:
        print('\n' + "Fundammental law violated. The code needs correction")
        break
