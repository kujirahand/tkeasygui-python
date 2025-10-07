"""Tests for popup_buttons"""

import TkEasyGUI as eg

food = eg.popup_buttons("What do you want to eat?", buttons=["Ramen", "Curry", "Pizz"])
eg.popup("Please eat " + food + ".")
