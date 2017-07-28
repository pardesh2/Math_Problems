#! /usr/bin/env python3

import math

def main():
    sphere = Sphere(1, (0, 0))
    cone = Cone(sphere.radius*math.sqrt(2), 4*sphere.radius)
    print('the radius of the sphere is %s and the radius of the cone is %s' % (sphere.radius, cone.radius))

    while True:
        new_radius = float(input('''Enter the radius of the cone or '0' to exit: '''))
        if new_radius == 0:
            break
        while new_radius <= sphere.radius:
            new_radius = float(input('''Radius of cone must be larger than radius of sphere. Enter the radius of the cone or '0' to exit: '''))
            if new_radius == 0:
                break
        if new_radius == 0:
            break
        cone_2 = Cone(new_radius, cone_generator(sphere, new_radius)[1])
        print(cone_generator(sphere, new_radius), 'volume of cone is %s and volume of sphere is %s' % (cone_2.volume(), sphere.volume()))

class Sphere(object):
    def __init__(self, radius, center_point):
        self.radius = radius
        self.center_point = center_point
    def volume(self):
        return 4/3 * math.pi * self.radius**3
       
class Cone(object):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
    def volume(self):
        return 1/3 * math.pi * self.radius**2 * self.height

def cone_generator(sphere, radius):
    new_height = (2*radius**2 * sphere.radius)/(radius**2 - 1) 
    new_volume = math.pi * radius**2 * new_height
    return (radius, new_height)

class Transformer(object):
    def __init__(self, multiplier):
        self.multiplier = multiplier
    def stretch_radius(self, cone):
        new_radius = cone.radius * self.multiplier
        new_height = new_radius + new_radius + (2*new_radius)/(self.multiplier**2 - 1)
        return (new_radius, new_height)

main()
