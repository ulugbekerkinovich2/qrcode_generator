import qrcode
import uuid
from io import BytesIO
import random
import time
from django.core.files.base import ContentFile

def generate_qr_code(data, file_name="qr_code.png"):
    """
    Generate a QR code image from the given data and return it as a ContentFile.
    
    Parameters:
    - data (str): The data to be encoded in the QR code.
    - file_name (str): The name of the file to save the QR code image.
    
    Returns:
    - ContentFile: A Django ContentFile containing the QR code image.
    """
    # Create a QR code object
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR Code; bigger size means it can hold more data
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=10,  # Size of each box in the QR code grid
        border=4,  # Thickness of the border (minimum is 4 for QR code standard)
    )
    
    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)  # Fit the QR code to the provided data
    
    # Create an image from the QR Code instance
    img = qr.make_image(fill='blue', back_color='yellow')
    
    # Save the image to a BytesIO buffer
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    
    # Create a Django ContentFile from the BytesIO buffer
    qr_code_file = ContentFile(buffer.getvalue(), name=file_name)
    
    return qr_code_file

# Example usage
qr_code = generate_qr_code("https://www.youtube.com/watch?v=4Ka_j1VWQO8", "qr_code.png")

# Save the QR code to a file
with open("qr_code.png", "wb") as f:
    f.write(qr_code.read())


def generate_unique_numeric_id():
    # Get the current time in milliseconds since the epoch and convert to a string
    current_time_ms = str(int(time.time() * 1000))
    
    # Generate a random number and convert to a string, zero-padded to ensure it has 3 digits
    random_number = str(random.randint(0, 999)).zfill(3)
    
    # Combine the time and random number, then take the last 12 characters to ensure the ID is 12 digits long
    unique_id = (current_time_ms + random_number)[-12:]

    return unique_id