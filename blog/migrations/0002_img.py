# Generated by Django 4.2 on 2023-04-27 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imageName', models.CharField(max_length=200)),
                ('imageDesc', models.TextField()),
                ('imageTime', models.DateTimeField(auto_now_add=True)),
                ('imageFile', models.ImageField(upload_to='upload_images/')),
            ],
        ),
    ]
