import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) 
#astuce Python pratique pour pouvoir importer des modules dans d'autres dossiers (comme view/) sans casser l'organisation du projet.

import unittest
from gpiozero import Device
from gpiozero.pins.mock import MockFactory

from view.platine import Platine


Device.pin_factory = MockFactory()

class TestPlatineTP4(unittest.TestCase):
    def setUp(self):
        self.platine = Platine()

    def test_bouton1_presse(self):
        self.platine.buttons["Bouton1"].pin.drive_low()
        self.assertTrue(self.platine.buttons["Bouton1"].is_active)

    def test_bouton2_presse(self):
        self.platine.buttons["Bouton2"].pin.drive_low()
        self.assertTrue(self.platine.buttons["Bouton2"].is_active)

    def test_bouton1_is_presse_false(self):
        self.platine.buttons["Bouton1"].pin.drive_high()
        self.assertFalse(self.platine.buttons["Bouton1"].is_active)

    def test_bouton2_is_presse_false(self):
        self.platine.buttons["Bouton2"].pin.drive_high()
        self.assertFalse(self.platine.buttons["Bouton2"].is_active)

if __name__ == "__main__":
    unittest.main()
