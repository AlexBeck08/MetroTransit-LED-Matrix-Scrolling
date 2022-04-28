# MetroTransit-LED-Matrix-Scrolling
Scrolling 64x32 LED Matrix for Metro Transit


## Products Used:
- [Raspberry Pi Zero 2 W](https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/)
- [Adafruit 64x32 P4 LED Matrix](https://www.adafruit.com/product/2278)
- [Adafruit RGB Matrix HAT + RTC](https://www.adafruit.com/product/2345)

## Resources Used:
- [Adafruit RGB Matrix Guide](https://learn.adafruit.com/adafruit-rgb-matrix-plus-real-time-clock-hat-for-raspberry-pi)
- [rpi-rgb-led-matrix by hzeller](https://github.com/hzeller/rpi-rgb-led-matrix)

## Instructions

1. Follow adafruit guide to get HAT and LED Matrix hooked up.
2. Use samples in Adafruit guide as well as hzeller repository to test out screen
3. create folder for these files and copy over rgbmatrix, samplebase, and fonts from the hzeller repository.
4. Use rollingBusGenius to get 4 routes and the next 3 buses for each route.
5. Use latestMatrix to get next 8 buses from any route at an intersection.
