import spidev
import time
from libsoc import gpio
from gpio_96boards import GPIO

GPIO_A = GPIO.gpio_id('GPIO_CS')
pins = (
 (GPIO_A, 'out'),
)

GPIO_B = GPIO.gpio_id(‘GPIO_B’)
pins = (
    (GPIO_B, ‘out’),
)

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=10000
spi.mode = 0b00
spi.bits_per_word = 8

def blink(gpio):
    gpio.digital_write(GPIO_B, GPIO.HIGH)
    time.sleep(1)
    gpio.digital_write(GPIO_B, GPIO.LOW)
    time.sleep(1)

def readpot(gpio):
    gpio.digital_write(GPIO_A, GPIO.HIGH)
    time.sleep(0.0002)
    gpio.digital_write(GPIO_A, GPIO.LOW)
    r = spi.xfer2([0x01, 0x80, 0x00])
    gpio.digital_write(GPIO_A, GPIO.HIGH)
    adcout = (r[1] << 8) & 0b1100000000
    adcout = adcout | (r[2] & 0xff)
    return adcout

    if adcout > 500.0:
	with GPIO(pins) as gpio:
	  blink(gpio)
    return adcout

while True:
 with GPIO(pins) as gpio:
     value = readpot(gpio)
     print("value = %d" % value)
     print(" ---------------------- " )
     time.sleep(0.5)
