from django.shortcuts import get_object_or_404
from django.http import FileResponse
from .models import Files

def serve_file(request, file_id):
    file = get_object_or_404(Files, id=file_id)
    return FileResponse(file.file)
