from django.contrib import admin
from .models import File, QrCode,UploadFile

@admin.register(File)
class FilesAdmin(admin.ModelAdmin):
    list_display = ('id', 'files')

@admin.register(QrCode)
class QrCodesAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'url_image']
@admin.register(UploadFile)
class UploadFilesAdmin(admin.ModelAdmin):
    list_display = ('id', 'file')