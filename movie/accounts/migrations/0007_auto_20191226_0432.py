# Generated by Django 2.0.2 on 2019-12-26 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20191226_0422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='banner_image',
            field=models.ImageField(help_text='Banner image for Movie', upload_to='image/'),
        ),
    ]
