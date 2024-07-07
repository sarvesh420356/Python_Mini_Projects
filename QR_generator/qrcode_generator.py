import qrcode

# Data to be added in qrcode
data = "https://www.linkedin.com/in/sarveshshinde2002"

# Generate QR code
qr = qrcode.QRCode(
    version=1,  # Version of the QR code (1 to 40, higher means more data capacity)
    # error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level (L, M, Q, H)
    box_size=10,  # Size of each box (pixel size)
    border=5,  # Border around the QR code (in boxes)
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Generate QR code image
qr_image = qr.make_image(fill="black", back_color="white")

# Save the QR code image
qr_image.save("test.png")
