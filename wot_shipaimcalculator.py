import  math
import FreeSimpleGUI as sg
import json



def calculate_projectilespeed(range,elevation_angle):
    g = 9.81
    range = range*10
    num = float(-45)
    if (elevation_angle > num):
        num = elevation_angle
    num = num*-1
    muzzle_velocity = math.sqrt(range*g/math.sin(2*num*float(0.017453292)))
    return muzzle_velocity



def  calcualte_leaddistance(ship_speed,target_speed,target_heading,ship_heading,muzzle_velocity,distance,t_bearing):
    ship_speed = ship_speed * 0.514444
    target_speed = target_speed * 0.514444
    distance = distance * 0.9144

    v_m = muzzle_velocity

    target_x_v = target_speed*math.cos(target_heading)
    target_y_v = target_speed*math.sin(target_heading)

    ship_x_v = ship_speed * math.cos(ship_heading)
    ship_y_v = ship_speed * math.sin(ship_heading)

    v_r_X = target_x_v-ship_x_v
    v_r_y = target_y_v-ship_y_v

    #v_r = math.sqrt((v_r_X**2)+(v_r_y**2))

    dx =  distance*math.cos(t_bearing)
    dy = distance * math.sin(t_bearing)


    a=(v_r_X**2)+(v_r_y**2)-(v_m**2)
    b=2*(dx*v_r_X+dy*v_r_y)
    c=(dx**2)+(dy**2)
    discriminant = b**2 - 4*a*c
    t = (-b + math.sqrt(discriminant)) / (2 * a)

    lead_distance_meters = target_speed * t


    return lead_distance_meters*1.09361





gun_dict = {}
with open("H:\\War on the Sea\\MODS\\TTE MAIN MOD 6.1.1 [WOTS 1.08g7]\\WarOnTheSea_Data\\StreamingAssets\\override\\unit\\sea\\mountData.txt","r", encoding='utf-8-sig') as file:


    for line in file:

        try:
            parsed_data = json.loads(line.strip())

            mount_id = parsed_data.get("mountID", "Unknown")

            max_range = parsed_data.get("maxRange", "Unknown")

            vertical_arc = parsed_data.get("verticalArc", "Unknown")
            gun_dict[mount_id] = [max_range, vertical_arc["x"]]





        except json.JSONDecodeError as e:
            print(f"Error parsing line: {line.strip()} - {e}")





# All the stuff inside your window.
layout = [
            [sg.Text('Gunnery solver')],
            [sg.Text("0", key='solution')],
            [sg.Text('Target distance: '), sg.InputText()],
            [sg.Text('Target speed: '), sg.InputText()],
            [sg.Text('Target heading: '), sg.InputText()],
            [sg.Text('Target bearing: '), sg.InputText()],
            [sg.Text('My ship heading:'), sg.InputText()],
            [sg.Text('My ship speed:'), sg.InputText()],
            [sg.DropDown(list(gun_dict), size=(20, 4), enable_events=False, key='gunmount')],
            [sg.Button('Ok'), sg.Button('Cancel'),sg.Button('Calculate')],

]

# Create the Window
window = sg.Window('Window Title', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    target_distance = int(values[0])
    target_speed = int(values[1])
    target_heading = int(values[2])
    target_bearing = int(values[3])
    my_shipheading = int(values[4])
    my_shipspeed = int(values[5])
    params_muzzle_v= gun_dict[values["gunmount"]]
    print(params_muzzle_v)

    if event == "Calculate":
        window['solution'].update(calcualte_leaddistance(my_shipspeed,target_speed,target_heading,my_shipheading,calculate_projectilespeed(params_muzzle_v[0],params_muzzle_v[1]),target_distance,target_bearing))

window.close()