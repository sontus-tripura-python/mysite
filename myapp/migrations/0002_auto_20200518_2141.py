# Generated by Django 3.0.6 on 2020-05-18 15:41

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
