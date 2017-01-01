from math import atan2, pi

from pyb import delay
from machine import I2C

import display
from imu.lsm303 import LSM303


def run_imu_test(i2c_bus=2):
    d = display.create_display()
    i2c = I2C(i2c_bus, freq=400000)
    devices = i2c.scan()
    lsm303 = LSM303(i2c)

    while True:
        accel, mag = lsm303.read()
        x, y, z = accel
        x, z, y = mag

        h = atan2(y, x) * 180.0 / pi

        d.fill_buffer(0)
        d.framebuf.text('N: {}'.format(h), 0, 0, 0x0F)
        d.send_buffer()

        delay(50)

