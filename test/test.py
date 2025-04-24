from gpiozero import Button
from time import sleep

# Boutons connectés aux GPIO 19 et 13
bouton1 = Button(19)
bouton2 = Button(13)

print("Test des boutons... (Appuie sur les boutons)")

try:
    while True:
        if bouton1.is_pressed:
            print("Bouton 1 pressé ✅")
        if bouton2.is_pressed:
            print("Bouton 2 pressé ✅")
        sleep(0.1)
except KeyboardInterrupt:
    print("\nTest terminé.")
