from django.shortcuts import get_object_or_404
from django.http import FileResponse
from .models import File

def serve_file(request, file_id):
    files = get_object_or_404(File, id=file_id)
    return FileResponse(files.file)
