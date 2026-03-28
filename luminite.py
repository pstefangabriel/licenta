import lgpio
import time

# chipul principal pentru pini pe PI5
CHIP_ID = 0
PIN_GPIO = 17

try:
    chip = lgpio.gpiochip_open(CHIP_ID)
    lgpio.gpio_claim_output(chip, PIN_GPIO)
    

    while True:
        print("ON")
        lgpio.gpio_write(chip, PIN_GPIO, 1)
        time.sleep(1)
        
        print("OFF")
        lgpio.gpio_write(chip, PIN_GPIO, 0)
        time.sleep(1)

except Exception as e:
    print(f"Eroare directă LGPIO: {e}")
except KeyboardInterrupt:
    lgpio.gpio_write(chip, PIN_GPIO, 0)
    lgpio.gpiochip_close(chip)
    print("\nProgram oprit corect.")