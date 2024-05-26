from django.contrib import admin
from .models import File, QrCode

@admin.register(File)
class FilesAdmin(admin.ModelAdmin):
    list_display = ('id', 'file')

@admin.register(QrCode)
class QrCodesAdmin(admin.ModelAdmin):
    list_display = ('id', 'image')
