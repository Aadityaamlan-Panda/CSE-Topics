# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 14:11:08 2026

@author: aadityaap22
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import math
import matplotlib.pyplot as plt
import cv2

image = cv2.imread('Picture2_lab4.png', cv2.IMREAD_GRAYSCALE)

plt.imshow(image, cmap='gray')
plt.title('Selfie Image')
print(image)
plt.show()

row,col = np.shape(image)

U, sigma, Vt = np.linalg.svd(image, full_matrices=False)
U.shape, sigma.shape, Vt.shape

n = 800

reconstructed = np.matrix(U[:, :n]) * np.diag(sigma[:n]) * np.matrix(Vt[:n, :])
print(n*(row+col))
plt.imshow(reconstructed, cmap='gray')
plt.title('n = %s' % n)
plt.show()
 


'''
def find_col_norm(V,pos,n):
    s = 0
    for i in range(n):
        s+=V[i][pos]*V[i][pos]
    
    s = math.sqrt(s)
    return s

def find_dot(A,Q,apos,qpos,n):
    s = 0
    for i in range(n):
        s+=A[i][apos]*Q[i][qpos]
    
    return s

def find_vec_norm(V,n):
    s = 0
    for i in range(n):
        s+=V[i]*V[i]
    
    s = math.sqrt(s)
    return s

def find_transpose(A,n,m):
    Atrp = np.zeros((m,n))
    for i in range(n):
        for j in range(m):
            Atrp[j][i] = A[i][j]
    return Atrp

def matrix_multiply(A1,A2,n,t,m):
    Ares = np.zeros((n,m))
    for i in range(n):
        for j in range(m):
            for k in range(t):
                Ares[i][j]+=(A1[i][k]*A2[k][j])
    return Ares

def extract_col(A,n,j):
    col_vec = np.zeros((n,1))
    for i in range(n):
        col_vec[i] = A[i][j]
    return col_vec

def const_x_matrix(A,n,m,const):
    for i in range(n):
        for j in range(m):
            A[i][j]*=const
            
    return A

def uv_prod(U,V,m,n):
    res = np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            res[i][j] = U[i]*V[j]
                
    return res

def matrix_sum(A,B,m,n):
    res = np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            res[i][j] = A[i][j] + B[i][j]
                
    return res

print('Taking the image as matrix: -')

A = image
n,m = np.shape(A)
print(n)
print(m)
N = m
Q = np.zeros((N,N))
R = np.zeros((N,N))

Atrp = find_transpose(A,n,m)
print(Atrp)
A_curr = matrix_multiply(Atrp,A,m,n,m)

print(A_curr)
Q_final = np.zeros((N,N))

for rep in range(20):
 Q = np.zeros((N,N))
# Finding q1
 norm_a1 = find_col_norm(A_curr,0,N)
 for i in range(N):
    Q[i][0] = A_curr[i][0]/norm_a1


#defining dp for overlapping subproblems....row stands for A and column stands for Q
 dp = np.zeros((N,N))
 vis = np.zeros((N,N))

# Finding qr
 for j in range(N):
    if j==0: 
        continue
    perp = np.zeros(N)
    for i in range(N):
        s = 0
        
        for r in range(j):
            
            if vis[j][r] == 0:
                dp[j][r] = find_dot(A_curr,Q,j,r,N)
                vis[j][r] = 1
                
            s+=dp[j][r]*Q[i][r]
            
        perp[i] = A_curr[i][j]-s
       
        
    
    perp_norm = find_vec_norm(perp,N) 
    
    for i in range(N):
        Q[i][j] = perp[i]/perp_norm
            
 #print(Q)
 
 if rep==0:
     Q_final = Q
 else:
     temp = matrix_multiply(Q_final,Q,N,N,N)
     Q_final = temp

#Finding R: Rij = Qi*Aj
 for i in range(N):
    for j in range(N):
     if i<=j:
        if vis[j][i]==0:
            dp[j][i] = find_dot(A_curr,Q,j,i,N)
            vis[j][r] = 1
        R[i][j] = dp[j][i]
 #print(R)
 A_curr = matrix_multiply(R, Q, N, N, N)

print("Printing A after "+str(rep)+"th repititions:-")
print(A_curr)

print("Printing Q after "+str(rep)+"th repititions:-")
print(Q_final)

V = Q_final

U = np.zeros((n,N))
sigma = np.zeros((N,N))
sigma_inv = np.zeros((N,N))
eps = 1e-10
for i in range(N):
    sigma[i][i] = math.sqrt(abs(A_curr[i][i]))
    if sigma[i][i] > eps:
        sigma_inv[i][i] = 1/sigma[i][i]

AV = matrix_multiply(A,V,n,m,N)
U = matrix_multiply(AV,sigma_inv,n,N,N)

for j in range(N):
    norm = find_col_norm(U,j,n)
    if norm>0:
        for i in range(n):
            U[i][j] = U[i][j]/norm

print("Printing U after "+str(rep)+"th repititions:-")
print(U)

print("Printing sigma after "+str(rep)+"th repititions:-")
print(sigma)

print("Printing V after "+str(rep)+"th repititions:-")
print(V)

print("Column norm of U")
nm = find_col_norm(U,0,N)
print(nm)

print("Column norm of V")
nm_ = find_col_norm(V,0,N)
print(nm_)

Vt = find_transpose(V,N,N)


num = 10
An = np.zeros((n,m))
for i in range(num):
 u_sig = uv_prod(U[:,i], V[:,i], n,m)
 curr_singular_image = const_x_matrix(u_sig, n, m, sigma[i][i])
 print(An)
 An = matrix_sum(An, curr_singular_image, n, m)


plt.imshow(An, cmap='gray')
plt.title('n = '+str(num))
plt.show()
'''