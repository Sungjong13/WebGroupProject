# Generated by Django 4.1.2 on 2022-11-01 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("board", "0002_post_image_delete_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="media/users_upload/%Y/%m/%d"
            ),
        ),
    ]