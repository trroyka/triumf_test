import simple_draw as sd
import math


def bone(start_point, angle, length, width, color1=sd.background_color, color2=sd.background_color):
    angle_rad = math.radians(angle)
    real_start = sd.get_point(start_point.x + width / 2 * math.sin(angle_rad),
                              start_point.y - width / 2 * math.cos(angle_rad))
    contur = (start_point, real_start,
              sd.get_point(real_start.x + length * math.cos(angle_rad), real_start.y + length * math.sin(angle_rad)),
              sd.get_point(real_start.x - width * math.sin(angle_rad) + length * math.cos(angle_rad),
                           real_start.y + width * math.cos(angle_rad) + length * math.sin(angle_rad)),
              sd.get_point(real_start.x - width * math.sin(angle_rad), real_start.y + width * math.cos(angle_rad))
              )
    sd.polygon(contur, color=color1, width=0)
    sd.lines(contur, color=color2, closed=True, width=2)


def joint_point(point11, point12, point21, point22):
    # уравнения прямых ax+by+c = 0
    a1 = point11.y - point12.y
    b1 = point12.x - point11.x
    c1 = point11.x * point12.y - point12.x * point11.y

    a2 = point21.y - point22.y
    b2 = point22.x - point21.x
    c2 = point21.x * point22.y - point22.x * point21.y

    # y = kx+g
    k1 = -a1 / b1
    g1 = -c1 / b1
    k2 = -a2 / b2
    g2 = -c2 / b2

    f_point_x = (g1 - g2) / (k2 - k1)
    f_point_y = k2 * f_point_x + g2
    return f_point_x, f_point_y


def sleeve(start_point, angle, angle2, length, width, color1, color2):
    # для наглядности http://joxi.ru/krDajB4IJ8Qkgm
    angle_rad = math.radians(angle)
    angle2_rad = math.radians(angle2)
    real_start = sd.get_point(start_point.x + width / 2 * math.sin(angle_rad),
                              start_point.y - width / 2 * math.cos(angle_rad))
    joint_center = sd.get_point(start_point.x + length * math.cos(angle_rad),
                                start_point.y + length * math.sin(angle_rad))
    a1_point = start_point
    a_point = sd.get_point(real_start.x - width * math.sin(angle_rad), real_start.y + width * math.cos(angle_rad))
    # пересчет точки B в зависимости от угла сгиба руки
    if angle2 - angle > 10:
        angle_b = angle + (angle2 - angle) / 10
        angle_b_rad = math.radians(angle_b)
        b_point = sd.get_point(a_point.x + length / 2 * math.cos(angle_b_rad),
                               a_point.y + length / 2 * math.sin(angle_b_rad))
    else:
        b_point = sd.get_point(a_point.x + length / 2 * math.cos(angle_rad),
                               a_point.y + length / 2 * math.sin(angle_rad))

    d_point = sd.get_point(joint_center.x - width / 2 * math.sin(angle2_rad) + length * math.cos(angle2_rad),
                           joint_center.y + width / 2 * math.cos(angle2_rad) + length * math.sin(angle2_rad))
    e_point = sd.get_point(d_point.x + width * math.sin(angle2_rad), d_point.y - width * math.cos(angle2_rad))
    g_point = real_start
    # пересчет точки C в зависимости от угла сгиба руки
    if angle2 - angle > 2:
        angle_c = angle - (angle2 - angle) / 5
        angle_c_rad = math.radians(angle_c)
        c1_point = sd.get_point(b_point.x + length / 2 * math.cos(angle_c_rad),
                                b_point.y + length / 2 * math.sin(angle_c_rad))
    else:
        c1_point = sd.get_point(b_point.x + length / 2 * math.cos(angle_rad),
                                b_point.y + length / 2 * math.sin(angle_rad))
    c2_point = sd.get_point(d_point.x - length * math.cos(angle2_rad), d_point.y - length * math.sin(angle2_rad))
    if angle2 == 0:
        c_point = c1_point

    elif angle2 == 90:
        c_point = c2_point
    else:
        c_points = joint_point(b_point, c1_point, d_point, c2_point)
        c_point = sd.get_point(c_points[0], c_points[1])

    f1_point = sd.get_point(e_point.x - length * math.cos(angle2_rad), e_point.y - length * math.sin(angle2_rad))
    f2_point = sd.get_point(real_start.x + length * math.cos(angle_rad), real_start.y + length * math.sin(angle_rad))
    if angle2 == 0:
        f_point = f1_point
    elif 89 < angle < 90:
        f_point = f1_point
    else:
        f_points = joint_point(e_point, f1_point, g_point, f2_point)
        f_point = sd.get_point(f_points[0], f_points[1])

    contur = (a1_point, a_point, b_point, c_point, d_point, e_point, f_point, g_point)
    sd.polygon(contur, color=color1, width=0)
    sd.lines(contur, color=color2, closed=True, width=2)


def arm(color1, color2, color3, angle1, angle2):
    try:
        # для костей характеристики
        start_bp_point = sd.get_point(200, 400)  # parent_bone
        bone_length = 300
        bone_width = 30
        angle1_rad = math.radians(angle1)
        start_cb_point = sd.get_point(start_bp_point.x + bone_length * math.cos(angle1_rad),
                                      start_bp_point.y + bone_length * math.sin(angle1_rad))  # child-bone
        # для рукава(мышц)
        sleeve_width = 80
        sleeve(start_point=start_bp_point, angle=angle1, angle2=angle2, length=bone_length, width=sleeve_width,
               color1=color3, color2=color2)
        bone(start_point=start_bp_point, angle=angle1, length=bone_length, width=bone_width, color1=color1,
             color2=color2)
        bone(start_point=start_cb_point, angle=angle2, length=bone_length, width=bone_width, color1=color1,
             color2=color2)
        # сустав
        joint_center = sd.get_point(
            start_bp_point.x + bone_length * math.cos(angle1_rad),
            start_bp_point.y + bone_length * math.sin(angle1_rad))
        sd.circle(center_position=joint_center, radius=bone_width / 2 + 10, color=color1, width=0)
        sd.circle(center_position=joint_center, radius=bone_width / 2 + 10, color=color2, width=2)

    except ZeroDivisionError:
        pass
