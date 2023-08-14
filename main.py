import qrcode

data = 'Cole seu conteúdo aqui'

img = qrcode.make(data)
img.save('E:/QRcode Generator/myqrcode.png')