import qrcode
from io import BytesIO
from django.core.files.base import ContentFile
from django.conf import settings
from django.db import models
import uuid

class File(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file = models.FileField(upload_to='files/')

    def __str__(self):
        return self.file.name

    def save(self, *args, **kwargs):
        print("saving...")
        # Call the original save method to ensure the file is saved
        super().save(*args, **kwargs)
        print("saving...1")
        # Generate QR code
        qr = qrcode.QRCode(
            
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        print("saving...2")
        # Construct the file URL
        file_url = f"http://{settings.ALLOWED_HOSTS[0]}:8000/certificate/{self.id}"
        qr.add_data(file_url)
        qr.make(fit=True)
        print("saving...3")
        # Create an image from the QR Code instance
        img = qr.make_image(fill='blue', back_color='white')
        print("saving...4")
        # Save the image to a BytesIO buffer
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        print("saving...5")
        # Create a Django ContentFile from the BytesIO buffer
        qr_code_file = ContentFile(buffer.getvalue(), name=f"{self.file.name}_qr.png")
        
        # Construct the full URL for the QR code image
        qr_code_url = f"http://{settings.ALLOWED_HOSTS[0]}:8000/media/qrcodes/{self.file.name}_qr.png"
        
        # Create and save the QrCodes instance
        QrCode.objects.create(files=self, image=qr_code_file, url_image=qr_code_url)

    class Meta:
        verbose_name = 'File'
        verbose_name_plural = 'Files'

class QrCode(models.Model):
    files = models.OneToOneField(File, on_delete=models.CASCADE, related_name='qrcode')
    image = models.ImageField(upload_to='qrcodes/')
    url_image = models.URLField(max_length=200)

    def __str__(self):
        return self.image.name

    class Meta:
        verbose_name = 'QrCode'
        verbose_name_plural = 'QrCodes'
