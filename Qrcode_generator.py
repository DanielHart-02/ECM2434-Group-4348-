import qrcode  
from pyzbar.pyzbar import decode
from PIL import Image

# Prompt the user to enter the content for the QR code
qr_content = input("Enter the content for the QR code: ")

# Generate the QR code
myqr = qrcode.make(qr_content)
myqr.save("myqr.png", scale=8)

# Open the generated QR code image
qr_image = Image.open("myqr.png").convert('L')  

# Decode the QR code
decoded_data = decode(qr_image)

# Check if QR code is decoded successfully and print the content
if decoded_data:
    print(decoded_data[0].data.decode("ascii"))
else:
    print("No QR code found.")
