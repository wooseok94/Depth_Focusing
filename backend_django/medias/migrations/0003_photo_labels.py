# Generated by Django 4.1.5 on 2023-02-04 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("medias", "0002_photo_depth_file_photo_seg_file"),
    ]

    operations = [
        migrations.AddField(
            model_name="photo",
            name="labels",
            field=models.JSONField(default=dict),
        ),
    ]
