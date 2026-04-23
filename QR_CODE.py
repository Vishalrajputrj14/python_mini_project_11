import qrcode as qr

img = qr.make("https://www.youtube.com/channel/UCWv7vMbMWH4-V0ZXdmDpPBA")
img.save("qr_code.png")