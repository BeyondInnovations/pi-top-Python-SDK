from pitop import Pitop
from time import sleep

pitop = Pitop()
miniscreen = pitop.miniscreen

miniscreen.display_image_file("/usr/lib/python3/dist-packages/pitop/miniscreen/images/rocket.gif")


sleep(2)

print("Saving to file...")
image = miniscreen.image
image.save("/home/pi/Desktop/My Miniscreen Rocket.gif")
