def matr_input():
    n, m = map(int, (input("Enter size of matrix:").split()))
    matrix1 = []
    print("Enter matrix:")
    for i in range(n):
        temp = list(map(float, input().split()))
        matrix1.append(temp)
    return n,m,matrix1    

def matr_output(n,m,matrix1):
    print("The result is:")
    for i in range(n):
        l=''
        for j in range(m):
            l += str(matrix1[i][j])+' '
        print(l)
        
def add_matr(n1, m1, mt1, mt2):
    mnew=mt1
    for i in range(n1):
        for j in range(m1):
            mnew[i][j] += mt2[i][j]
    return mnew

def matr_mult_num(n1, m1, mt1, num):
    mnew=mt1
    for i in range(n1):
        for j in range(m1):
            mnew[i][j] *= num
    return mnew

def mult_matr(n1, m1, mt1, n2, m2, mt2):
    mnew = [([0]*m2) for i in range(n1)]
    for i in range(n1):
        for j in range(m2):
            for k in range(m1):
                mnew[i][j] += mt1[i][k] * mt2[k][j] 
    return mnew

def matr_transp1(n1, m1, mt1):
    mnew = [([0]*n1) for i in range(m1)]
    for i in range(n1):
        for j in range(m1):
            mnew[i][j] = mt1[j][i]
    return mnew

def matr_transp2(n1, m1, mt1):
    mnew = [([0]*n1) for i in range(m1)]
    for i in range(n1):
        for j in range(m1):
            mnew[i][j] = mt1[m1-j-1][n1-i-1]
    return mnew

def matr_transp3(n1, m1, mt1):
    for i in range(n1):
        for j in range(m1//2):
            mt1[i][j], mt1[i][m1-j-1] =  mt1[i][m1-j-1],mt1[i][j]
    return mt1

def matr_transp4(n1, m1, mt1):
    for i in range(n1//2):
        for j in range(m1):
            #print(mt1[i][j])
            mt1[i][j], mt1[n1-i-1][j] =  mt1[n1-i-1][j], mt1[i][j]
    return mt1

def matr_determ(A, total=0):
    indices = list(range(len(A)))
    if len(A) == 1 and len(A[0]) == 1:
        return A[0][0]
    
    if len(A) == 2 and len(A[0]) == 2:
        val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
        return val
 
    for fc in indices: 
        As = A 
        As = As[1:] 
        height = len(As)  
 
        for i in range(height): 
            As[i] = As[i][0:fc] + As[i][fc+1:] 
 
        sign = (-1) ** (fc % 2) 
        sub_det = matr_determ(As)
        total += sign * A[0][fc] * sub_det 
 
    return total

def task1():
    "matr1+matr2"
    n1,m1, matr1 = matr_input()
    n2,m2, matr2 = matr_input()
    if n1==n2 and m1==m2:
        madd = add_matr(n1, m1, matr1, matr2)
        matr_output(n1,m1,madd)
    else:
        print("The operation cannot be performed.")

def task2():
    "matr1 x num"
    n1,m1, matr1 = matr_input()
    num = float(input("Enter constant: "))
    mnum = matr_mult_num(n1, m1, matr1, num)
    matr_output(n1,m1,mnum)

def task3():
    "matr1 x matr2"
    n1,m1, matr1 = matr_input()
    n2,m2, matr2 = matr_input()
    if m1==n2:
        mmult = mult_matr(n1, m1, matr1, n2, m2, matr2)
        matr_output(n1,m2,mmult)
    else:
        print("The operation cannot be performed.")

def task5():
    "matr1 determinant"
    n1,m1, matr1 = matr_input()
    print("The result is:")
    print(matr_determ(matr1))

def task4():
    m = menu2()
    if m == 1:
        task41()
    elif m==2:
        task42()
    elif m==3:
        task43()
    elif m==4:
        task44()
    else:
        print("Wrong choice!")
        

def task41():
    n1,m1, matr1 = matr_input()
    mtr = matr_transp1(n1, m1, matr1)
    matr_output(m1,n1,mtr)


def task42():
    n1,m1, matr1 = matr_input()
    mtr = matr_transp2(n1, m1, matr1)
    matr_output(m1,n1,mtr)
    
def task43():
    n1,m1, matr1 = matr_input()
    mtr = matr_transp3(n1, m1, matr1)
    matr_output(n1,m1,mtr)

def task44():
    n1,m1, matr1 = matr_input()
    mtr = matr_transp4(n1, m1, matr1)
    matr_output(n1,m1,mtr)

def matr_minor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def matr_inverse(m):
    determinant = matr_determ(m)
    #special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]

    #find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = matr_minor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * matr_determ(minor))
        cofactors.append(cofactorRow)
    cofactors = matr_transp1(len(m), len(m[0]), cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors


def task6():
    n1,m1, matr1 = matr_input()
    matr_m1 = matr_inverse(matr1)
    matr_output(m1,n1,matr_m1)
    

def menu():
    print("\n1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("4. Transpose matrix")
    print("5. Calculate a determinant")
    print("6. Inverse matrix")
    print("0. Exit")
    choice = int(input("Your choice:"))
    return choice


def menu2():
    print("\n1. Main diagonal")
    print("2. Side diagonal")
    print("3. Vertical line")
    print("4. Horizontal line")
    choice = int(input("Your choice:"))
    return choice

       

m = menu()
while m != 0:
    if m == 1:
        task1()
    elif m==2:
        task2()
    elif m==3:
        task3()
    elif m==4:
        task4()
    elif m==5:
        task5()
    elif m==6:
        task6()        
    else:
        print("Wrong choice!")
    m = menu()  
