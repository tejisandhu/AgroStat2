# Generated by Django 5.0.2 on 2024-05-03 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0028_alter_register_profile_picture"),
    ]

    operations = [
        migrations.AlterField(
            model_name="register",
            name="profile_picture",
            field=models.ImageField(
                blank=True, default="DP_1.jpg", upload_to="ProfilePictures"
            ),
        ),
    ]
