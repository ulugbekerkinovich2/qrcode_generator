from django.contrib import admin
from .models import Files, QrCodes

@admin.register(Files)
class FilesAdmin(admin.ModelAdmin):
    list_display = ('id', 'file')

@admin.register(QrCodes)
class QrCodesAdmin(admin.ModelAdmin):
    list_display = ('id', 'image')
