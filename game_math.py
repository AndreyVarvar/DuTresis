from settings import *


def sort_by_depth(cam_pos: vec3, planes: list[vec3]):
    planes.sort(key=lambda plane: cam_pos.distance_to(vec3(sum([v.x for v in plane])/len(plane),
                                                           sum([v.y for v in plane])/len(plane),
                                                           sum([v.z for v in plane])/len(plane))))

    return planes


def project_point_to_plane(plane_normal_vec: vec3, plane_normal_vec_origin: vec3, point: vec3):
    v = point - plane_normal_vec_origin
    d = v.x*plane_normal_vec.x + v.y*plane_normal_vec.y + v.z*plane_normal_vec.z
    projected_point = point - d*plane_normal_vec

    return projected_point
