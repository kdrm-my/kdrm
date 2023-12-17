import qrcode 

#Data for which you want to make
#Here we are using the URL of some website
data = "https://web.facebook.com/profile.php?id=61554909320880"

#File name of the qr code image
#Change it with your desired file name
QRCodefile = "Facebook.png"

#Generating the QR code
QRimage = qrcode.make(data)

#Saving image into a file
QRimage.save(QRCodefile)