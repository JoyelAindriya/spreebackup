# Generated by Django 4.0 on 2024-02-13 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0005_alter_manage_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manage',
            name='img',
            field=models.ImageField(null=True, upload_to='image'),
        ),
    ]
