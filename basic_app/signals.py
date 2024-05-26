import qrcode
from io import BytesIO
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.files.base import ContentFile
from django.conf import settings
from .models import Files, QrCodes

@receiver(post_save, sender=Files)
def generate_qr_code(sender, instance, created, **kwargs):
    if created:
        # Create a QR code object
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        # Construct the file URL
        file_url = f"http://{settings.ALLOWED_HOSTS[0]}:8000/certificate/{instance.id}"
        qr.add_data(file_url)
        qr.make(fit=True)

        # Create an image from the QR Code instance
        img = qr.make_image(fill='blue', back_color='white')
        
        # Save the image to a BytesIO buffer
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        
        # Create a Django ContentFile from the BytesIO buffer
        qr_code_file = ContentFile(buffer.getvalue(), name=f"{instance.file.name}_qr.png")
        
        # Construct the full URL for the QR code image
        qr_code_url = f"http://{settings.ALLOWED_HOSTS[0]}:8000/media/qrcodes/{instance.file.name}_qr.png"
        
        # Create and save the QrCodes instance
        QrCodes.objects.create(file=instance, image=qr_code_file, url_image=qr_code_url)
