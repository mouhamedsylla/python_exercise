# 1e méthode
"""def convertir_hex_en_rgb(hex : str) -> tuple:
    red = int(hex[1:3], 16)
    green = int(hex[3:5], 16)
    blue = int(hex[5:7], 16)
    print("(",red, green, blue,")")
convertir_hex_en_rgb("#B12345")"""

# 2e methode
from PIL import ImageColor
val_hex = input("entrer: ")
def convertir_hex_en_rgb(hex):
    rgb = ImageColor.getcolor(hex, "RGB")
    print(type(rgb))
convertir_hex_en_rgb(val_hex)

# convert string in hex
"""rgb = input()  # string val 
an_int = int(rgb, 16) # string convert to int
an_hex = hex(an_int)  # int convert to hex
"""
"""rgb = input()
def convert(hex: str) -> tuple:
    red = int(hex[1:3], 16)
    green = int(hex[3:5], 16)
    blue = int(hex[5:7], 16)
    rgb_tuple = []
    rgb_tuple.extend([red, green, blue])
    print(max(rgb_tuple))

convert(rgb)"""