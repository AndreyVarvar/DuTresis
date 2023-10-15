from settings import *


class Object:
    def __init__(self, vertices: list, color: vec3):
        self.vertices = vertices
        self.color = color


class Cube(Object):
    """
    cube object, since all of the cubes should have
    no rotation attribute needed, since the cubes do not rotate, instead, it is the camera that is rotating.
    """
    def __init__(self, pos=vec3(0, 0, 0), side_length=100, color=vec3(255, 255, 255)):
        self.pos = pos
        self.side_length = side_length

        super().__init__(self.create_vertices(pos, side_length), color)

    @staticmethod
    def create_vertices(pos, a):
        """
        make vertices for a cube object
        :param pos: position of the center of the cube
        :param a: side length
        :return: vertices
        """
        b = a/2  # since i need a length from the center of the cube to it's size, i need half the  length of the side
        x1 = pos.x+b
        x2 = pos.x-b
        y1 = pos.y-b
        y2 = pos.y+b
        z1 = pos.z+b
        z2 = pos.z-b

        # each element of the list has 3 point, creating a triangle in the 3d space
        vertices = [[vec3(x2, y1, z2), vec3(x2, y1, z1), vec3(x1, y1, z1)],
                    [vec3(x1, y1, z1), vec3(x1, y1, z2), vec3(x2, y1, z2)],

                    [vec3(x2, y2, z2), vec3(x2, y1, z2), vec3(x1, y1, z2)],
                    [vec3(x1, y1, z2), vec3(x1, y2, z2), vec3(x2, y2, z2)],

                    [vec3(x2, y2, z2), vec3(x2, y2, z1), vec3(x1, y2, z1)],
                    [vec3(x1, y2, z1), vec3(x1, y2, z2), vec3(x2, y2, z2)],

                    [vec3(x2, y1, z1), vec3(x2, y2, z1), vec3(x1, y2, z1)],
                    [vec3(x1, y2, z1), vec3(x1, y1, z1), vec3(x2, y1, z1)],

                    [vec3(x1, y2, z2), vec3(x1, y1, z2), vec3(x1, y1, z1)],
                    [vec3(x1, y1, z1), vec3(x1, y2, z1), vec3(x1, y2, z2)],

                    [vec3(x2, y2, z1), vec3(x2, y1, z1), vec3(x2, y1, z2)],
                    [vec3(x2, y1, z2), vec3(x2, y2, z2), vec3(x2, y2, z1)]]
        
        return vertices
