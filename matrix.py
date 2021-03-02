"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    for col in range(len(matrix[0])):
        column=[matrix[i][col] for i in range(len(matrix))]
        print(*column)

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i==j:
                matrix[i][j]=1
            else:
                matrix[i][j]=0
    pass

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    ans=[]
    for i in range(len(m2)):
        ans.append(len(m1)*[0])
    for i in range(len(m1[0])):
        for j in range(len(m2)):
            for k in range(len(m1)):
                ans[j][i]+=m1[k][i]*m2[j][k]
    for i in range(len(m2)):
        for j in range(len(m2[0])):
            m2[i][j]=ans[i][j]




def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
