# Generated by Django 4.0.4 on 2022-05-14 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=500)),
                ('img', models.ImageField(upload_to='index/Footer_comments')),
                ('author', models.CharField(max_length=30)),
                ('livein', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='slider',
            name='img',
            field=models.ImageField(upload_to='index/slider'),
        ),
    ]
