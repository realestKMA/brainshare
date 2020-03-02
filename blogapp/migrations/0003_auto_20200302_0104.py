# Generated by Django 3.0.3 on 2020-03-02 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_auto_20200301_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='social',
            name='platform',
            field=models.CharField(blank=True, choices=[('Facebook', 'Facebook'), ('Twitter', 'Twitter'), ('Instagram', 'Instagram'), ('Tumblr', 'Tumblr'), ('LinkedIn', 'LinkedIn'), ('Pinterest', 'Pinterest'), ('Telegram', 'Telegram'), ('YouTube', 'YouTube'), ('Discord', 'Discord'), ('Github', 'Github')], help_text='Select a social media platform', max_length=100, null=True, verbose_name='Platform'),
        ),
    ]
