# Generated by Django 3.2.5 on 2021-07-30 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0013_alter_resume_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='address',
            field=models.CharField(default='address', max_length=100),
        ),
        migrations.AlterField(
            model_name='resume',
            name='email',
            field=models.EmailField(default='gmail.com', max_length=30),
        ),
    ]
