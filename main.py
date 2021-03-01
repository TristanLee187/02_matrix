from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix=new_matrix()

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
test_matrix_op()
draw_lines( matrix, screen, color )
display(screen)