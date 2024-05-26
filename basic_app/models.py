from django.db import models
import uuid

class Files(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file = models.FileField(upload_to='files/')

    def __str__(self):
        return self.file.name

    class Meta:
        verbose_name = 'File'
        verbose_name_plural = 'Files'

class QrCodes(models.Model):
    file = models.OneToOneField(Files, on_delete=models.CASCADE, related_name='qrcode')
    image = models.ImageField(upload_to='qrcodes/')
    url_image = models.URLField(max_length=200)

    def __str__(self):
        return self.image.name

    class Meta:
        verbose_name = 'QrCode'
        verbose_name_plural = 'QrCodes'
