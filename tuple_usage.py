# encoding:utf-8
# @date:
# @author: vicky
# @environment:
# @brief:

"""tuple unpacking"""
lax_coordinates = (33.464537, 172.93836)
latitude, longitude = lax_coordinates
print(latitude)
print(longitude)

metro_areas = [
    ('tokyo', 'JP', 36.933, (35.78, 139.36)),
    ('mexico city', 'MX', 20.142, (19.433, -99.133))
]
print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'

for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0:
        print(fmt.format(name, latitude, longitude))

"""namedtuple"""
from collections import namedtuple
# building a namedtuple
# 1. the name: like City
# 2. the elements name:like name country population coordinate
City = namedtuple('City', 'name country population coordinate')
tokyo = City('tokyo', 'JP', 38.747, (37.3375, 138.37))
print(tokyo)
print(tokyo.population)
print(tokyo.coordinate)
print(tokyo[1])
# the attribution of namedtuple
print(City._fields)



"""using * to deal the last of the elements in a tuple"""
a, b, *rest = range(5)
print(a, b, rest)

a, *rest, b = range(5)
print(a, rest, b)



