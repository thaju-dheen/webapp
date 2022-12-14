# Generated by Django 4.0.2 on 2022-02-24 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='img')),
                ('roll', models.CharField(max_length=200)),
                ('desc', models.TextField()),
                ('fb_link', models.URLField()),
                ('inst_link', models.URLField()),
                ('twt_link', models.URLField()),
                ('wk_link', models.URLField()),
            ],
        ),
    ]
