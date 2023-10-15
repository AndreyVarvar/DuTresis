from settings import *
from game_math import *


class Camera:
    """
    IMPORTANT:
    the camera frame has a different position blitting. The origin in in the middle of the screen, and y axis is not inverted
    """
    def __init__(self, camera_plane_size, pos=vec3(0, 0, 0), normal=vec3(1, 0, 0)):
        # the z-axis rotation is disabled, so no need to worry about that

        self.up = vec3(0, 1, 0)
        self.right = vec3(1, 0, 0)
        self.forward = vec3(0, 0, 1)

        self.pos = pos
        self.normal = normal
        self.rotation = vec3(radians(self.normal.angle_to(self.right)),
                             radians(self.normal.angle_to(self.up)),
                             radians(self.normal.angle_to(self.forward)))

        self.cam_plane_size = camera_plane_size
        self.frame_origin = vec2(self.cam_plane_size.x//2, self.cam_plane_size.y//2)

        self.frame = pg.Surface(camera_plane_size)


        self.planes_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 0, 255), (255, 255, 0), (0, 255, 255),
                              (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 0, 255), (255, 255, 0), (0, 255, 255)]

    def render_object(self, obj):
        vertices = obj.vertices
        color = obj.color

        rotation_x = vec3(cos(radians(self.normal.angle_to(self.right)+90)),
                          0,
                          sin(radians(self.normal.angle_to(self.right)+90)))

        # depth_sorted_vertices = sort_by_depth(self.pos, vertices)

        for i, plane in enumerate(vertices):
            # step 1: project the plane onto the camera plane
            projected_plane = []

            for point in plane:
                # this formula is taken from here: https://stackoverflow.com/questions/9605556/how-to-project-a-point-onto-a-plane-in-3d
                n = self.normal

                v = self.pos - point
                d = v.x*n.x + v.y*n.y + v.z*n.z


                projected_point = point + d*n

                projected_plane.append(projected_point)

            display_plane = []

            for projected_point in projected_plane:
                # find the vector of the point relative to the self.normal origin (self.pos)
                projected_point_v = self.pos - projected_point

                # find the angle between rotation_x and the vector of the projected point
                ang = radians(projected_point_v.angle_to(rotation_x))

                # we know the angle from the horizontal line and the length of the vector, that means we can find the coordinatess of the point on the plane
                d = projected_point_v.length()
                display_point = vec2(d*cos(ang) + self.frame_origin.x, -d*sin(ang) + self.frame_origin.y)

                display_plane.append(display_point)

            # finally draw the plane
            pg.draw.polygon(self.frame, self.planes_colors[i], display_plane)



    def process_events(self, keys_pressed):
        angular_velocity = 0.1

        self.rotation = vec3(radians(self.normal.angle_to(self.right)),
                             radians(self.normal.angle_to(self.up)),
                             radians(self.normal.angle_to(self.forward)))

        self.actual_circle_radius = cos(self.rotation.y)

        if keys_pressed[pg.K_LEFT]:
            self.normal.x = cos(self.rotation.x + angular_velocity*self.actual_circle_radius)
            self.normal.z = cos(self.rotation.z + angular_velocity*self.actual_circle_radius)

        if keys_pressed[pg.K_RIGHT]:
            self.normal.x = cos(self.rotation.x - angular_velocity*self.actual_circle_radius)
            self.normal.z = cos(self.rotation.z - angular_velocity*self.actual_circle_radius)

        if keys_pressed[pg.K_UP] and self.normal.y < 0.9:
            self.normal.y = sin(self.rotation.y + angular_velocity)

        if keys_pressed[pg.K_DOWN] and self.normal.y > -0.9:
            self.normal.y = sin(self.rotation.y - angular_velocity)

    def reset_frame(self):
        self.frame.fill((255, 255, 255))

