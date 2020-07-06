# Generated by Django 3.0.3 on 2020-07-06 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_user_about_me'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='about_me',
            field=models.TextField(blank=True, default='', help_text='Over here, write few things about yourself that you think will interest those that read your post and check out your profile.Feel free.', null=True, verbose_name='About me'),
        ),
    ]
