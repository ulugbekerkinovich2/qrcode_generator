# from django.shortcuts import get_object_or_404
# from django.http import FileResponse
# from .models import File

# def serve_file(request, file_id):
#     print(f"File ID: {file_id}")
#     file_instance = get_object_or_404(File, id=file_id)
#     print(f"File instance: {file_instance}")
#     return FileResponse(file_instance.files.open(), as_attachment=True, filename=file_instance.files.name)


from django.shortcuts import get_object_or_404
from django.http import FileResponse
from .models import File

def serve_file(request, file_id):
    print(f"File ID: {file_id}")
    file_instance = get_object_or_404(File, id=file_id)
    print(f"File instance: {file_instance}")

    # Open the file using the file field's path
    response = FileResponse(file_instance.files.open(), filename=file_instance.files.name)
    response['Content-Disposition'] = f'inline; filename="{file_instance.files.name}"'
    return response
