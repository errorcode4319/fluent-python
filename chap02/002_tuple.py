from collections import namedtuple 

def used_as_record():
    lax_coordinates = (33.9425, -118.408056)
    city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
    traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
    for passport in sorted(traveler_ids):
        print('%s/%s' % passport)


def unpack1():

    def divmod(x, y):
        return (x // y, x % y)
    
    t = (20, 8)
    quotient, remainder = divmod(*t) # * => Unpack 
    print(quotient, remainder) # 2, 4

def unpack2():
    a, b, *rest = range(5)
    print(a, b, rest)   # 0 1 [2, 3, 4]
    a, b, *rest = range(2)
    print(a, b, rest)   # 0 1 []

    # only one available
    a, *body, c, d = range(5)
    print(a, body, c, d)
    *head, b, c, d = range(5)
    print(head, b, c, d)    # [0, 1] 2, 3, 4

def unpack3():
    metro_areas = [
        ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
        ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
        ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ]

    for name, cc, pop, (latitude, longitude) in metro_areas: # Unpack inner tuple 
        print(name, latitude, longitude)

def named_tuple():
    City = namedtuple('City', 'name country population coordinates')
    tokyo = City('Tokyo', 'JP', '36.933', (35.689722, 139.691667))
    print(tokyo)

    print(City._fields)
    LatLong = namedtuple('LatLong', 'lat long')
    delhi_data = ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889))
    delhi = City._make(delhi_data)
    for key, value in delhi._asdict().items():
        print(key + ':', value)

if __name__ == "__main__":
    used_as_record() 
    unpack1() 
    unpack2() 
    unpack3()
    named_tuple() 