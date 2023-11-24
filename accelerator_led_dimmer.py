
import time
import board

# setup Gyroscope and Accelerometer
from adafruit_lsm6ds.lsm6dsox import LSM6DSOX
i2c = board.I2C()  # uses board.SCL and board.SDA
sensor = LSM6DSOX(i2c)

# setup LED PWM
import pwmio
led = pwmio.PWMOut(board.LED, frequency=5000, duty_cycle=0)

def set_led_brightness(brightness):
    # led.duty_cycle is a 16-bit value that controls the brightness of the LED.
    duty_cycle = int(brightness * 2**16 / 3000)  # 2**16==65535 is the max value for duty_cycle
    if duty_cycle >= 65535:
        duty_cycle = 65535
    if duty_cycle <= 0:
        duty_cycle = 0
    led.duty_cycle = duty_cycle

    time.sleep(0.01)


if __name__ == "__main__":
    # turn off power led

    brightness=100
    set_led_brightness(brightness)
    time.sleep(1)
    set_led_brightness(0)
    while True:
        x_acc, y_acc, z_acc = sensor.acceleration
        #print(f"Acceleration: X:{x_acc}, Y: {y_acc} Z: {z_acc} m/s^2")
        #print("Gyro X:%.2f, Y: %.2f, Z: %.2f radians/s" % (sensor.gyro))
        # Print  so that the the line updates instead of scrolls
        #time.sleep(0.5)
        # Map z_acc from 0 to 9.8 to 0 to 100

        if z_acc < 0:
            brightness = 0
        brightness = int(z_acc * 100 / 9.8)
        #print(f"zacc:{z_acc}, brightness:{brightness}")
        set_led_brightness(brightness)




