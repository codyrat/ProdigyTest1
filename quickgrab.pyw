import ImageGrab
import os
import time

x_pad = 464
y_pad = 241

def screenGrab():
    """
    All coordinates assume a screen resolution of 1280x1024, and Chrome 
    maximized with the Bookmarks Toolbar enabled.
    Down key has been hit 4 times to center play area in browser.
    x_pad = 464
    y_pad = 241
   """

    box = (x_pad+1, y_pad+1,x_pad+640, y_pad+481)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
            '.png', 'PNG')


def main():
    screenGrab()


if __name__ == '__main__':
    main()

