import simple_draw as sd
import functions as fn


def fitness():
    start_angle1 = 0
    start_angle2 = 0
    while True:
        sd.start_drawing()
        fn.arm(color1=sd.background_color, color2=sd.background_color, color3=sd.background_color,
               angle1=start_angle1, angle2=start_angle2)
        if (start_angle1 + 0.5) % 45 < 0.9:
            start_angle1 = start_angle1 - 0.4
        else:
            start_angle1 = start_angle1 - 0.2
        if (start_angle2 + 0.5) % 45 < 0.9:
            start_angle2 = start_angle2 + 0.8
        else:
            start_angle2 = start_angle2 + 0.4
        fn.arm(color1=(169, 169, 169), color2=(105, 105, 105), color3=(244, 164, 96), angle1=start_angle1,
               angle2=start_angle2)
        sd.finish_drawing()
        sd.sleep(0.01)
        if start_angle2 - start_angle1 > 130:
            break

    while True:
        sd.start_drawing()
        fn.arm(color1=sd.background_color, color2=sd.background_color, color3=sd.background_color,
               angle1=start_angle1, angle2=start_angle2)
        if (start_angle1 + 0.5) % 45 < 0.9:
            start_angle1 = start_angle1 + 0.4
        else:
            start_angle1 = start_angle1 + 0.2
        if (start_angle2 + 0.5) % 45 < 0.9:
            start_angle2 = start_angle2 - 0.8
        else:
            start_angle2 = start_angle2 - 0.4
        fn.arm(color1=(169, 169, 169), color2=(105, 105, 105), color3=(244, 164, 96), angle1=start_angle1,
               angle2=start_angle2)
        sd.finish_drawing()
        sd.sleep(0.01)
        if start_angle2 - start_angle1 < 0:
            break
