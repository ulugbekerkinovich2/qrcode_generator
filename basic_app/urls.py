from django.urls import path
from .views import serve_file

urlpatterns = [
    path('certificate/<uuid:file_id>', serve_file, name='serve_file'),
]
