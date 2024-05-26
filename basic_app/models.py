import qrcode
from io import BytesIO
from django.core.files.base import ContentFile
from django.conf import settings
from django.db import models
from utils.app import generate_unique_numeric_id

def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='blue', back_color='white')
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    return ContentFile(buffer.getvalue())

class File(models.Model):
    id = models.CharField(max_length=12, unique=True, default=generate_unique_numeric_id, primary_key=True, editable=False)
    files = models.FileField(upload_to='files/')

    def __str__(self):
        return self.files.name

    def save(self, *args, **kwargs):
        request = kwargs.pop('request', None)
        # Call the original save method to ensure the file is saved
        super().save(*args, **kwargs)
        print(request)
        host = 5000
        scheme = "http://127.0.0.1"
        # Generate QR code
        file_url = f"{scheme}:{host}/certificate/{self.id}"
        qr_code_file = generate_qr_code(file_url)
        qr_code_file.name = f"{self.files.name}_qr.png"
        
       
        # Construct the full URL for the QR code image
        qr_code_url = f"{scheme}:{host}/media/qrcodes/{self.files.name}_qr.png"
        
        # Create and save the QrCode instance
        QrCode.objects.create(file=self, image=qr_code_file, url_image=qr_code_url)

    class Meta:
        verbose_name = 'File'
        verbose_name_plural = 'Files'

class QrCode(models.Model):
    file = models.OneToOneField(File, on_delete=models.CASCADE, related_name='qrcode')
    image = models.ImageField(upload_to='qrcodes/')
    url_image = models.URLField(max_length=200)

    def __str__(self):
        return self.image.name

    class Meta:
        verbose_name = 'QrCode'
        verbose_name_plural = 'QrCodes'


class UploadFile(models.Model):
    file = models.FileField(upload_to='files/')

    def __str__(self):
        return self.file.name
    
    class Meta:
        verbose_name = 'UploadFile'
        verbose_name_plural = 'UploadFiles'