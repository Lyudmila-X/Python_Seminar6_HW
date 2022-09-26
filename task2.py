# Самая далекая планета
from cmath import pi

data = open("input2.txt", "r")
orbits = list(map(lambda x: tuple(float(item) for item in (x.strip().split(","))), data.readlines()))
def find_farthest_orbit (list_of_orbits):
    farthest_orbit = ()
    squares_orbits = [(pi*item[0]*item[1]) for item in list_of_orbits if item[0]!=item[1]]
    max_square = max(squares_orbits)
    farthest_orbit = list(filter(lambda x: (pi*x[0]*x[1]) == max_square, list_of_orbits))[0]
    return farthest_orbit

print(find_farthest_orbit(orbits))
data.close
