from gpiozero import LED
import time

# Pinul 11 fizic este GPIO 17
comanda = LED(17)

print("Sistem pornit! Clipim de 10 ori...")

try:
    for i in range(10):
        comanda.on()
        print(f"Bliț {i+1}: ON")
        time.sleep(0.3)
        comanda.off()
        print(f"Bliț {i+1}: OFF")
        time.sleep(0.3)
except KeyboardInterrupt:
    comanda.off()

print("Test terminat.")