# -----------------------------------------------------------
# demonstrates generation of a basic QR code using the qrcode module
#o
# (C) 2026 Frank Hofmann, Freiburg, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# 
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
#
# inspired by: Generate QR Code using qrcode in Python
# https://www.geeksforgeeks.org/python/generate-qr-code-using-qrcode-in-python/
# -----------------------------------------------------------

import qrcode

# define data to encode
data = "Hello, world!"

# create QR code object
qr = qrcode.QRCode()

# add data
qr.add_data(data)

# generate the QR code
qr.make()

# generate an image from the QR code
image = qr.make_image()

# save image as file
image.save("/tmp/qrcode.png")
