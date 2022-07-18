import qrcode

img = qrcode.make('http://www.naodongopen.com')
img.show()

"""
version: value [1, 40] size of binCode, 1 -> 21x21 matrix

ERROR_CORRECT_L
ERROR_CORRECT_M
ERROR_CORRECT_Q
ERROR_CORRECT_H

box_size: number of pixels in each box of binCode
border: number of boxes of side (default is 4), distance of binCode to image
"""
qr = qrcode.QRCode(
	version=1,
	error_correction=qrcode.constants.ERROR_CORRECT_L,
	box_size=10,
	border=4,
	)
qr.add_data('http://www.naodongopen.com')
qr.make(fit=True)

img = qr.make_image(fill_color='green', back_color='white')
img.show()

from PIL import Image

icon = Image.open('/data/wanglei/Kodak_png/kodim23.png')

img_w, img_h = img.size

factor = 4
size_w = int(img_w/factor)
size_h = int(img_h/factor)
icon_w, icon_h = icon.size

if icon_w > size_w:
	icon_w =size_w

if icon_h > size_h:
	icon_h =size_h

icon =icon.resize((icon_w, icon_h), Image.ANTIALIAS)

w =int((img_w -icon_w) /2)
h =int((img_h -icon_h) /2)

img.paste(icon, (w, h), icon)

img.show()

img.save("qrcode.png")