def make_list1():
    symbols = '!@#$%'
    codes = []
    for symbol in symbols:
        codes.append(ord(symbol))
    return codes 

def make_list2():
    symbols = '!@#$%'
    return [ord(symbol) for symbol in symbols]

def make_list3(): # slower than make_list2 
    symbols = '!@#$%'
    return list(filter(lambda c: c > 127, map(ord, symbols)))

def cartesian_product():
    colors = ['black', 'white']
    sizes = ['S', 'M', 'L']
    tshirts = [(color, size) for color in colors 
                                for size in sizes]
    return tshirts 

def cartesian_product_generator(): # No List Instance
    colors = ['black', 'white']
    sizes = ['S', 'M', 'L']
    for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
        print(tshirt)

if __name__ == "__main__":
    print(cartesian_product())
    cartesian_product_generator()

    x = 'ABC'
    dummy = [ord(x) for x in x] # x in other scoped
    print(x)
    print(dummy)