# Generated by Django 4.0 on 2024-02-09 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manage',
            name='description',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='manage',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
