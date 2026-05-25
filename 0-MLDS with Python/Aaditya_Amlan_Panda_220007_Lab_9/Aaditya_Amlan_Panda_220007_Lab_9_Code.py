import numpy as np
np.set_printoptions(precision=3, suppress=True)
def find_mean(X):
    n = len(X)
    s = 0.0
    for i in range(n):
        s += X[i]
    return s/n

def find_variance(X, mean):
    n = len(X)
    s = 0.0
    for i in range(n):
        s += (X[i] - mean)**2
    return s/n

def find_Z_score(X):
    n,m = X.shape
    Z = np.zeros((n,m))
    for j in range(m):
        mean = find_mean(X[:,j])
        variance = find_variance(X[:,j], mean)
        for i in range(n):
            if variance!=0:
                Z[i,j] = (X[i,j] - mean)/np.sqrt(variance)
            else:
                Z[i,j] = 0.0
    return Z

def find_transpose(X):
    n,m = X.shape
    T = np.zeros((m,n))
    for i in range(n):
        for j in range(m):
            T[j,i] = X[i,j]
    return T

def find_w(E,u):
    n,m = E.shape
    w = np.zeros(m)
    Et = find_transpose(E)
    for i in range(m):
        s = 0.0
        for j in range(n):
            s += Et[i,j]*u[j]
        w[i] = s
    return w

def find_t(E,w):
    n,m = E.shape
    t = np.zeros(n)
    for i in range(n):
        s = 0.0
        for j in range(m):
            s += E[i,j]*w[j]
        t[i] = s
    return t

def find_c(F,t):
    n,m = F.shape
    c = np.zeros(m)
    Ft = find_transpose(F)
    for i in range(m):
        s = 0.0
        for j in range(n):
            s += Ft[i,j]*t[j]
        c[i] = s
    return c

def find_u(F,c):
    n,m = F.shape
    u = np.zeros(n)
    for i in range(n):
        s = 0.0
        for j in range(m):
            s += F[i,j]*c[j]
        u[i] = s
    return u

def find_p(E,t):
    n,m = E.shape
    p = np.zeros(m)
    Et = find_transpose(E)
    for i in range(m):
        s = 0.0
        for j in range(n):
            s += Et[i,j]*t[j]
        p[i] = s
    return p

def find_b(t,u):
    n = len(t)
    s = 0.0
    for i in range(n):
        s += t[i]*u[i]
    return s

def find_diff_norm(t,t_old):
    n = len(t)
    s = 0.0
    for i in range(n):
        s += (t[i] - t_old[i])**2
    return np.sqrt(s)

def find_norm(t):
    n = len(t)
    s = 0.0
    for i in range(n):
        s += t[i]**2
    return np.sqrt(s)


def find_outer_product(x,y):
    n = len(x)
    m = len(y)
    op = np.zeros((n,m))
    for i in range(n):
        for j in range(m):
            op[i,j] = x[i]*y[j]
    return op

def dot_product(x,y):
    n = len(x)
    s = 0.0
    for i in range(n):
        s += x[i]*y[i]
    return s

def matrix_multiply(A,B):
    n = A.shape[0]
    m = B.shape[1]
    p = A.shape[1]
    C = np.zeros((n,m))
    for i in range(n):
        for j in range(m):
            s = 0.0
            for k in range(p):
                s += A[i,k]*B[k,j]
            C[i,j] = s
    return C

def sum_of_squares(X):
    n,m = X.shape
    s = 0.0
    for i in range(n):
        for j in range(m):
            s += X[i,j]**2
    return s

Y = np.array([[14,7,8],
              [10,7,6],
              [8,5,5],
              [2,4,7],
              [6,2,4]])

X = np.array([[7,7,13,7],
             [4,3,14,7],
             [10,5,12,5],
             [16,7,11,3],
             [13,3,10,3]])

E = X.copy()
F = Y.copy()
E = find_Z_score(E)
F = find_Z_score(F)
print("Z-score of X:\n", E)
print("Z-score of Y:\n", F)

SSX = sum_of_squares(E)
SSY = sum_of_squares(F)

iterlim = 5
U = []
T = []
W = []
C = []
P = []
B = np.zeros((iterlim,iterlim))
Var = np.zeros((iterlim,4))

for itermax in range(iterlim):  
 u = np.ones(E.shape[0])
 iter = 0
 t = u.copy()
 while True:
    t_old = t.copy()
    u_old = u.copy()
    w = find_w(E,u)
    w = w/find_norm(w)
    t = find_t(E,w)
    t = t/find_norm(t)
    c = find_c(F,t)
    c = c/find_norm(c)
    u = find_u(F,c)
    if find_diff_norm(t,t_old) < 1e-6 and find_diff_norm(u,u_old) < 1e-6:
        break
    iter += 1
    
 b = find_b(t,u)
 p = find_p(E,t)

 Var[itermax,0] = dot_product(p,p)/SSX*100
 Var[itermax,2] = b**2/SSY*100
 
 if itermax > 0:
        Var[itermax,1] = Var[itermax-1,1] + Var[itermax,0]
        Var[itermax,3] = Var[itermax-1,3] + Var[itermax,2]
 else:
        Var[itermax,1] = Var[itermax,0]
        Var[itermax,3] = Var[itermax,2]
 
 U.append(u.copy())
 T.append(t.copy())
 W.append(w.copy())
 C.append(c.copy())
 P.append(p.copy())
 B[itermax,itermax] = b
 E = E - find_outer_product(t,p)
 F = F - b*find_outer_product(t,c)

 if itermax == 1:
     B_pls_2 = matrix_multiply(np.linalg.pinv(find_transpose(np.column_stack(P))),matrix_multiply(B[0:2,0:2],find_transpose(np.column_stack(C))))
     print("B_pls with 2 latent variables:\n", B_pls_2)

 if itermax == 2:
     B_pls_3 = matrix_multiply(np.linalg.pinv(find_transpose(np.column_stack(P))),matrix_multiply(B[0:3,0:3],find_transpose(np.column_stack(C))))
     print("B_pls with 3 latent variables:\n", B_pls_3)


print("Final U:\n", np.array(U))
print("Final T:\n", np.array(T))
print("Final W:\n", np.array(W))
print("Final C:\n", np.array(C))
print("Final P:\n", np.array(P))
print("Final B:\n", np.array(B))

B_pls = matrix_multiply(np.linalg.pinv(find_transpose(np.column_stack(P))),matrix_multiply(B,find_transpose(np.column_stack(C))))
print("B_pls with " + str(iterlim) + " latent variables:\n", B_pls)

X_hat = matrix_multiply(np.column_stack(T),find_transpose(np.column_stack(P)))
Y_hat = matrix_multiply(np.column_stack(T),matrix_multiply(B,find_transpose(np.column_stack(C))))

print("X fitted:\n", X_hat)
print("Y fitted:\n", Y_hat)

print("Variance explained in X:\n", Var[:,0])
print("Cumulative variance explained in X:\n", Var[:,1])
print("Variance explained in Y:\n", Var[:,2])
print("Cumulative variance explained in Y:\n", Var[:,3])
