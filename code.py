import win32api, win32con
import time

x_pad = 464
y_pad = 241

"""

Plate cords:

    92, 210
    193, 210
    295, 210
    397, 210
    490, 210
    599, 210
    
    phone = (592, 364)
    menu_toppings = (528, 274)
    menu_rice = (535, 293)
    menu_sake = (519, 317)

    buy_rice = (545, 284)

    t_shrimp = (489, 225)
    t_unagi = (472, 221)
    t_nori = (492, 284)
    t_roe = (576, 276)
    t_salmon = (491, 335)
    t_exit = (560, 335)

     
    delivery_norm = (593, 295)
    delivery_express = (582, 297)

"""

"""
Recipes:

onigiri
2
rice, 1
nori

caliroll:
1
rice, 1
nori, 1
roe

gunkan:
1
rice, 1
nori, 2
roe
"""
class Cord:
    f_shrimp = (35, 335)
    f_rice = (95, 335)
    f_nori = (38, 389)
    f_roe = (97, 394)
    f_salmon = (36,445)
    f_unagi = (91,444)


def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print "Click."          #completely optional. But nice for debugging purposes.


def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.1)
    print 'left Down'


def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(.1)
    print 'left release'


def mousePos(cord):
    win32api.SetCursorPos(x_pad + cord[0], y_pad + cord[1])


def get_cords():
    x, y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print x, y


def clear_tables():
    mousePos((92, 210))
    leftClick()

    mousePos((192, 210))
    leftClick()

    mousePos((295, 210))
    leftClick()

    mousePos((397, 210))
    leftClick()

    mousePos((490, 210))
    leftClick()

    mousePos((599, 210))
    leftClick()
    time.sleep(1)


def startGame():
    # location of first menu
    mousePos((315, 206))
    leftClick()
    time.sleep(.1)

    # location of second menu
    mousePos((315, 392))
    leftClick()
    time.sleep(.1)

    # location of third menu
    mousePos((315, 392))
    leftClick()
    time.sleep(.1)

    # location of fourth menu
    mousePos((583, 452))
    leftClick()
    time.sleep(.1)


def main():
    pass


if __name__ == '__main__':
    main()

