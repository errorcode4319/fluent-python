import dis 

def operate_add_mul():
    l = [1, 2, 3]
    print(l * 5) # 1 2 3 1 ... 2 3
    print('abcd' * 3) # abcdabcdab...cd


def multidimensional_list():
    board = [['_'] * 3 for i in range(3)]
    board[1][2] = 'X'
    print(board)
    '''
    board = []
    for i in range(3):
        row = ['_'] * 3
        board.append(row)
    '''

    weird_board = [['_'] * 3] * 3
    weird_board[1][2] = 'X'
    print(weird_board)  # Weird Result
    '''
    row = ['_'] * 3
    board = []
    for i in range(3):
        board.append(row)
    '''


def augmented_assignment():
    # += => __iadd__()
    # *= => __imul__()
    # i means in-place 
    l = [1, 2, 3]
    print(id(l), l)
    l *= 2 
    print(id(l), l) # Same ID, l.__imul__(2)

    t = (1, 2, 3)
    print(id(t), t) 
    t *= 2 
    print(id(t), t) # Diff ID, t = t * 2 (no __imul__ method in tuple)

    t = (1, 2, [30, 40])
    try:
        t[2] += [50, 60]
    except Exception as e:
        print(e)    # Exception!
    print(t) # but, t has been modified, ref: http://www.pythontutor.com/

    dis.dis('s[a] += b')

if __name__ == "__main__":
    multidimensional_list() 
    augmented_assignment() 