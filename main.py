from display import *
from draw import *
from matrix import *

def test_matrix_op():
    m2 = new_matrix(rows=0,cols=0)
    add_edge(m2,1,2,3,4,5,6)
    print('Testing add_edge. Adding (1, 2, 3), (4, 5, 6) m2 =')
    print_matrix(m2)

    m1=new_matrix()
    ident(m1)
    print('Testing ident. m1 =')
    print_matrix(m1)

    matrix_mult(m1,m2)
    print('Testing Matrix mult. m1 * m2 =')
    print_matrix(m2)

    m1=new_matrix(rows=0,cols=0)
    add_edge(m1,1,2,3,4,5,6)
    add_edge(m1,7,8,9,10,11,12)
    print('Testing Matrix mult. m1 =')
    print_matrix(m1)
    print('Testing Matrix mult. m2 =')
    print_matrix(m2)

    matrix_mult(m1,m2)
    print('Testing Matrix mult. m1 * m2 =')
    print_matrix(m2)

def my_own():
    screen = new_screen()
    color = [0, 0, 255]
    matrix=new_matrix(rows=0,cols=0)

    back_mat=new_matrix(rows=0,cols=0)
    test_mat=new_matrix(rows=0,cols=0)

    density=10
    p1=YRES//2
    p2=0
    for i in range(0,YRES//2,density):
        add_edge(back_mat,0,p1,0,p2,YRES,0)
        add_edge(back_mat,0,YRES-p1,0,p2,0,0)
        add_edge(back_mat, XRES, p1, 0, YRES-p2, YRES, 0)
        add_edge(back_mat, XRES, YRES - p1, 0, YRES-p2, 0, 0)
        add_edge(test_mat,p2,YRES//2,0,XRES//2,p1,0)
        add_edge(test_mat,p2,YRES//2,0,XRES//2,YRES-p1,0)
        add_edge(test_mat, XRES-p2, YRES // 2, 0, XRES // 2, p1, 0)
        add_edge(test_mat, XRES-p2, YRES // 2, 0, XRES // 2, YRES-p1, 0)
        p1+=density
        p2+=density

    test_trans=[
        [2,0,0,0],
        [0,2,0,0],
        [0,0,2,0],
        [0,0,0,2]
    ]
    for i in range(2):
        for j in range(0,len(back_mat),2):
            add_edge(matrix,back_mat[j][0],back_mat[j][1],back_mat[j][2],
                     back_mat[j+1][0],back_mat[j+1][1],back_mat[j+1][2])
        matrix_mult(test_trans,back_mat)

    for j in range(0, len(test_mat), 2):
        add_edge(matrix, test_mat[j][0], test_mat[j][1], test_mat[j][2],
                 test_mat[j + 1][0], test_mat[j + 1][1], test_mat[j + 1][2])

    point=2
    for i in range(0,len(matrix),2):
        draw_lines(matrix[i:i+2],screen,color)
        if color[point]==255:
            point=2-point
        color[point]+=5
        if point==0:
            color[point-1]-=5
        else:
            color[point-2]-=5
    display(screen)

test_matrix_op()
my_own()