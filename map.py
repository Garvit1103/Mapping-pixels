import pyautogui as pg
import time

mapped_array = [[(320, 216), (640, 216), (960, 216), (1280, 216), (1600, 216)], 
                [(320, 432), (640, 432), (960, 432), (1280, 432), (1600, 432)], 
                [(320, 648), (640, 648), (960, 648), (1280, 648), (1600, 648)], 
                [(320, 864), (640, 864), (960, 864), (1280, 864), (1600, 864)]]

#The above array corresponds to the 20 points that the current mouse position is being mapped to.

def calc_distance(a, b, c, d):
    return ((a-c)**2 + (b-d)**2)*0.5

#The above code is a function that calculates the distance between the points (a, b) and (c, d)

def return_closest_point(a, b):
    closest_point = (320, 216)
    for i in range(4):
        for j in range(5):
            if calc_distance(a, b, closest_point[0], closest_point[1]) > calc_distance(a, b, mapped_array[i][j][0], mapped_array[i][j][1]):
                closest_point = (mapped_array[i][j])
    return closest_point

#The above code calculates the nearest points by using a linear search algorithm by calculating the distance of the current mouse position and all the points and it returns the point which is the closest.

def convert_to_signal(index):
    return ((int(index[0]/320)-1) + ((int(index[1]/216))-1)*5)

#The above function, when used returns an integer to which the nearest point maps, so that it can be easily transmitted to Arduino.
#It's converting a 2-D array to a 1-D array.

led_status = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#The above array is directly being passed to the Arduino board in real time.

def print_led(led_stat):
    print(f'{led_stat[0]} {led_stat[1]} {led_stat[2]} {led_stat[3]} {led_stat[4]}')
    print(f'{led_stat[5]} {led_stat[6]} {led_stat[7]} {led_stat[8]} {led_stat[9]}')
    print(f'{led_stat[10]} {led_stat[11]} {led_stat[12]} {led_stat[13]} {led_stat[14]}')
    print(f'{led_stat[15]} {led_stat[16]} {led_stat[17]} {led_stat[18]} {led_stat[19]}')

#This is for displaying the 2-D grid which can be used for debugging.

while 1:
    for i in range(20):
        if i == (convert_to_signal(return_closest_point(pg.position()[0], pg.position()[1]))):
            led_status[i] = 1
        else:
            led_status[i] = 0
    print_led(led_status)
    print("")
    time.sleep(0.2)

#The above code reads and maps the current mouse position to the 20-LED grid.





