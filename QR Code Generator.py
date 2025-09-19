import qrcode

#take input from the user
data = input("Enter your links: ").strip()

#name the png file
file_name = input("enter your file name: ").strip()

#create a QRCode object in the same style
qr = qrcode.QRCode(version = 1,
                   box_size = 10,  #slightly smaller boxes
                   border = 5)  #slightly smaller border

#add the data
qr.add_data(data)

#make the QR code
qr.make(fit = True)

# generate the image with colors
img = qr.make_image(fill_color = 'black',back_color = 'white')

#save the file
img.save(f"{file_name}.png")