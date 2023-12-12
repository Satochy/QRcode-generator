import qrcode

img = qrcode.make('https://github.com/Satochy') # link que será o qrcode

type(img)
img.save("myqrcode.png") # nome do imagem .png com o qr code
