def stride():
    s = 'bicycle'
    # s[a, b, c] -> c: stride 
    print(s[::3])   # bye 
    print(s[::-1])  # elcycib
    print(s[::-2])  # eccb 


def allocate():
    l = list(range(10))
    l[2:5] = [20, 30]
    print(l)    # 0 1 20 30 5 6 7 8 9
    del l[5:7]
    print(l)    # 0 1 20 30 5 8 9
    l[3::2] = [11, 22]
    print(l)    # 0 1 20 11 5 22 9
    l[2:5] = [100] # 0 1 100 22 9
    print(l)
    # l[2:5] = 100  // TypeError: Can only assign an iterable 


if __name__ == '__main__':
    stride() 
    allocate() 