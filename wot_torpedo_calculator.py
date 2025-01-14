import FreeSimpleGUI as sg
import math


def calculate_lead_point(target_distance,target_speed,torpedo_speed,target_bearing,target_heading,our_heading):

     target_speed_mps = target_speed * 0.514444
     torpedo_speed_mps = torpedo_speed * 0.514444
     target_distance = target_distance
     #
     # aob = target_heading-target_bearing
     #
     # t = target_distance/(torpedo_speed_mps-target_speed_mps*math.cos(math.radians(aob)))
     #
     # lead_distance = target_speed_mps*t
     #
     #
     # # Intercept point in global coordinates (relative to map)
     # x_intercept = target_distance * math.cos(math.radians(target_bearing)) + lead_distance * math.cos(
     #     math.radians(target_heading))
     # y_intercept = target_distance * math.sin(math.radians(target_bearing)) + lead_distance * math.sin(
     #     math.radians(target_heading))
     #
     # # Calculate true bearing to intercept point
     # intercept_angle_rad = math.atan2(y_intercept, x_intercept)
     # intercept_angle_deg = (math.degrees(intercept_angle_rad) + 360) % 360  # Normalize to [0, 360)

     # v_m = torpedo_speed_mps
     #
     # target_x_v = target_speed_mps * math.cos(target_heading)
     # target_y_v = target_speed_mps * math.sin(target_heading)
     #
     # ship_x_v = 0 * math.cos(our_heading)
     # ship_y_v = 0 * math.sin(our_heading)
     #
     # v_r_X = target_x_v - ship_x_v
     # v_r_y = target_y_v - ship_y_v
     #
     # # v_r = math.sqrt((v_r_X**2)+(v_r_y**2))
     #
     # dx = target_distance * math.cos(target_bearing)
     # dy = target_distance * math.sin(target_bearing)
     #
     # a = (v_r_X ** 2) + (v_r_y ** 2) - (v_m ** 2)
     # b = 2 * (dx * v_r_X + dy * v_r_y)
     # c = (dx ** 2) + (dy ** 2)
     # discriminant = b ** 2 - 4 * a * c
     #
     # if a < 0:
     #
     #    t = (-b - math.sqrt(discriminant)) / (2 * a)
     # else:
     #    t = (-b + math.sqrt(discriminant)) / (2 * a)
     #
     # lead_distance_meters = t * target_speed
     #
     # print(f"Target speed (m/s): {target_speed_mps}")
     # print(f"Torpedo speed (m/s): {torpedo_speed_mps}")
     # print(f"Relative velocity X: {v_r_X}, Y: {v_r_y}")
     # print(f"dx: {dx}, dy: {dy}")
     # print(f"a: {a}, b: {b}, c: {c}")
     # print(f"Discriminant: {discriminant}")



     t = target_distance/torpedo_speed_mps


     lead_distance_meters = t*target_speed_mps


     x_intercept = target_distance * math.cos(math.radians(target_bearing)) + lead_distance_meters * math.cos(math.radians(target_heading))
     y_intercept = target_distance * math.sin(math.radians(target_bearing)) + lead_distance_meters * math.sin(math.radians(target_heading))


     intercept_angle_rad = math.atan2(y_intercept, x_intercept)
     intercept_angle_deg = (math.degrees(intercept_angle_rad) + 360) % 360

     return lead_distance_meters,intercept_angle_deg





# All the stuff inside your window.
layout = [  [sg.Text('Gunnery solver')],
            [sg.Text("0", key='solution')],
            [sg.Text('Target distance: '), sg.InputText()],
            [sg.Text('Target speed: '), sg.InputText()],
            [sg.Text('Target heading: '), sg.InputText()],
            [sg.Text('Target bearing: '), sg.InputText()],
            [sg.Text('Torpedo speed: '), sg.InputText()],
            [sg.Text('Ship heading: '), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    target_distance = int(values[0])
    target_speed = int(values[1])
    torpedo_speed = int(values[4])
    torpedo_heading = int(values[2])
    torpedo_bearing = int(values[3])
    my_heading = int(values[5])

    if target_distance != 0 and target_speed != 0 and torpedo_speed != 0:
        window['solution'].update(calculate_lead_point(target_distance,target_speed,torpedo_speed,torpedo_bearing,torpedo_heading,my_heading))

window.close()