from django.urls import path
from .views import serve_file

urlpatterns = [
    path('certificate/<int:file_id>', serve_file, name='serve_file'),
]
