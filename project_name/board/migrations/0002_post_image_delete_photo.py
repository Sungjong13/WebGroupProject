# Generated by Django 4.1.2 on 2022-11-01 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("board", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
        migrations.DeleteModel(name="Photo",),
    ]
