import os

# pentru PI5
os.environ['GPIOZERO_PIN_FACTORY'] = 'lgpio'

from gpiozero import LED
from gpiozero.pins.lgpio import LGPIOFactory
import time

# chipul 0 controleagza pinii
factory = LGPIOFactory(chip=0)

try:
    leduri = LED(17, pin_factory=factory)
    
    while True:
        print("Stare: APRINS (1)")
        leduri.on()
        time.sleep(1)
        
        print("Stare: STINS (0)")
        leduri.off()
        time.sleep(1)

except Exception as e:
    print(f"Eroare la nivel de chip: {e}")
except KeyboardInterrupt:
    print("\nTest terminat. Pinul a fost eliberat.")