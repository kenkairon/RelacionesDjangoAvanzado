# Generated by Django 5.2 on 2025-04-10 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_cover_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='address',
            field=models.TextField(null=True),
        ),
    ]
