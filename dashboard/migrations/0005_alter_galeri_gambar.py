# Generated by Django 4.1.7 on 2023-06-25 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_wisata_jenis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galeri',
            name='gambar',
            field=models.ImageField(null=True, upload_to='../dashboard/image_upload'),
        ),
    ]
