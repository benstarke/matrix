# Generated by Django 3.2 on 2021-05-30 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CAREER',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('Photo', models.FileField(upload_to='photos')),
                ('Description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Executive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('E_Photo', models.ImageField(upload_to='exec')),
                ('E_Title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Images', models.FileField(upload_to='gallery')),
            ],
        ),
    ]
