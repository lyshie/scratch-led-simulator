# coding=utf-8
from __future__ import unicode_literals

from blockext import *
from copy import deepcopy


class LED:

    def __init__(self):
        # buffer
        self.led = [[0 for x in range(8)] for y in range(8)]
        # final output
        self.output = [[0 for x in range(8)] for y in range(8)]
        # current location
        self.x = 0
        self.y = 0

    def _on_reset(self):
        print("""
        Reset! The red stop button has been clicked,
        And now everything is how it was.
        """)

    @command("set led ( %n , %n ) on", defaults=[0, 0])
    def set_led_on(self, x, y):
        self.led[x][y] = 1

    @command("set led ( %n , %n ) off", defaults=[0, 0])
    def set_led_off(self, x, y):
        self.led[x][y] = 0

    @command("locate led ( %n , %n )", defaults=[0, 0])
    def locate_led(self, x, y):
        self.x = x
        self.y = y

    @reporter("get location x")
    def get_location_x(self):
        return self.x

    @reporter("get location y")
    def get_location_y(self):
        return self.y

    @reporter("get led status")
    def get_led_status(self):
        return self.output[self.x][self.y]

    @reporter("status")
    def status(self):
        return self.output

    @command("flush")
    def flush(self):
        self.output = deepcopy(self.led)

descriptor = Descriptor(
    name="Simple 8x8 LED Matrix Extension",
    port=12345,
    blocks=get_decorated_blocks_from_class(LED),
    menus=dict(
    )
)

extension = Extension(LED, descriptor)

if __name__ == "__main__":
    extension.run_forever(debug=True)
