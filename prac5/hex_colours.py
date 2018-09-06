COLOUR_TO_HEX = {'aliceblue': '#fof8ff', 'antiquewhite': '#faebd7', 'aquamarine': '#7fffd4', 'azure': '#f0ffff',
                 'beige': '#f5f5dc', 'bisque': 'ffe4c4', 'black': '#000000', 'blue': '#0000ff', 'blueviolet': '8a2be2'}

colour = input("Enter colour: ").lower()
while colour != "":
    if colour in COLOUR_TO_HEX:
        print(colour, "is", COLOUR_TO_HEX[colour])
    else:
        print("colour not listed")
    colour = input("Enter colour: ").lower()
