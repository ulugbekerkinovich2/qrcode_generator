# Generated by Django 4.2.13 on 2024-05-26 17:45

from django.db import migrations, models
import django.db.models.deletion
import utils.app


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.CharField(default=utils.app.generate_unique_numeric_id, editable=False, max_length=12, primary_key=True, serialize=False, unique=True)),
                ('files', models.FileField(upload_to='files/')),
            ],
            options={
                'verbose_name': 'File',
                'verbose_name_plural': 'Files',
            },
        ),
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='files/')),
            ],
            options={
                'verbose_name': 'UploadFile',
                'verbose_name_plural': 'UploadFiles',
            },
        ),
        migrations.CreateModel(
            name='QrCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='qrcodes/')),
                ('url_image', models.URLField()),
                ('file', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='qrcode', to='basic_app.file')),
            ],
            options={
                'verbose_name': 'QrCode',
                'verbose_name_plural': 'QrCodes',
            },
        ),
    ]
