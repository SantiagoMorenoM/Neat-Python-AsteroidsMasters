# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 10:55:23 2022

@author: Santiago
"""

import re
import time
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT


def main(cascaded, block_orientation, rotate):
    
    #create matrix device
    serial = spi(port=0, device=1, gpio=noop())
    device = max7219(serial, cascaded=cascaded or 1, block_orientation=block_orientation, rotate=rotate or 1)
    # debugging purpose
    print("[-] Matrix initialized")
    
    # print hello world on the matrix display
    msg = "Y que no me digan en la esquina 'EL VENAO, EL VENAO' que eso a mi me mortifica"
    # debugging purpose
    print("[-] Printing: %s" % msg)
    show_message(device, msg, fill="red", font=proportional(CP437_FONT), scroll_delay=0.1)

if __name__ == "__main__":
    #cascaded= Number of cascaded MAX7219 LED matrices, default=1
    #block_orientation = choices 0, 90, -90, Corrects block orientation when wired vertically, default=0
    # rotate = choices 0, 1, 2, 3, Rotate display 0=0° , 1=90°, 2=180° 3=270°, default=0
        try:
            main(cascade=0, block_orientation=180, rotate=0)
        except KeyboardInterrupt:
            pass