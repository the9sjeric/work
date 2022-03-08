x1, y1, x2, y2 = 0, 0, 1920, 1080

from PIL import Image, ImageGrab
img_ready = ImageGrab.grab((x1, y1, x2, y2))
img_ready.show()
img_ready.save('aaa.jpg')