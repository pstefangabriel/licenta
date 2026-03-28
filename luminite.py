import os
# pentru PI 5
os.environ['GPIOZERO_PIN_FACTORY'] = 'lgpio'

from gpiozero import LED
import time

# GPIO 17 
try:
    led_comanda = LED(17)
    print("Succes! Am preluat controlul pinului GPIO 17 pe Pi 5.")
    
    while True:
        print("LED-uri: ON")
        led_comanda.on()
        time.sleep(1)
        
        print("LED-uri: OFF")
        led_comanda.off()
        time.sleep(1)

except Exception as e:
    print(f"Eroare neasteptata: {e}")
except KeyboardInterrupt:
    led_comanda.off()
    print("\nProgram oprit.")