# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import math

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

print('Enter the number of rows = number of columns and then enter the elements at every position')
N = int(input('Enter the number of rows = number of columns:'))

A = np.zeros((N,N))
for i in range(N):
    for j in range(N):
        A[i][j] = float(input("Enter element at position "+str(i)+","+str(j)+":"))
print (find_col_norm(A,0,N))
print(find_dot(A,A,0,1,N))

Q = np.zeros((N,N))
R = np.zeros((N,N))

# Finding q1
norm_a1 = find_col_norm(A,0,N)
for i in range(N):
    Q[i][0] = A[i][0]/norm_a1
    
print(norm_a1)
print(Q)

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
                dp[j][r] = find_dot(A,Q,j,r,N)
                vis[j][r] = 1
                
            s+=dp[j][r]*Q[i][r]
            
        perp[i] = A[i][j]-s
       
        
    
    perp_norm = find_vec_norm(perp,N) 
    
    for i in range(N):
        Q[i][j] = perp[i]/perp_norm
            
print(Q)

#Finding R: Rij = Qi*Aj
for i in range(N):
    for j in range(N):
     if i<=j:
        if vis[j][i]==0:
            dp[j][i] = find_dot(A,Q,j,i,N)
            vis[j][r] = 1
        R[i][j] = dp[j][i]
print(R)