# -----------------------------------------------------------
# demonstrates generation of a QR code with image using both the 
# qrcode module, and the Python Imaging Library (PIL)
#o
# (C) 2026 Frank Hofmann, Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# 
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
#
# inspired by: How to generate QR Codes with a custom logo using Python ?
# https://www.geeksforgeeks.org/python/how-to-generate-qr-codes-with-a-custom-logo-using-python/
# -----------------------------------------------------------

import qrcode
from PIL import Image

# define data to encode
data = "Python is cool"

# define link to logo that will appear in the centre of the QR code
logoLink = "python-logo.png"
logo = Image.open(logoLink)

# define base width of the QR code, and rescale the image
basewidth = 50
widthPercent = (basewidth/float(logo.size[0]))
heightSize = int((float(logo.size[1])*float(widthPercent)))
logo = logo.resize((basewidth, heightSize), Image.ANTIALIAS)

# create QR code object
qr = qrcode.QRCode()

# add data
qr.add_data(data)

# adjust error correction, and set to high
QRcode = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H
)

# generate the QR code
qr.make()

# generate an image from the QR code
image = qr.make_image(
    fill_color="orange",
    back_color="white"
).convert('RGB')

# set size of QR code
pos = ((image.size[0] - logo.size[0]) // 2,
       (image.size[1] - logo.size[1]) // 2)
image.paste(logo, pos)

# save image as file
image.save("/tmp/qrcode-with-image.png")
