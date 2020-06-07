# Generated by Django 3.0.3 on 2020-05-31 22:27

from django.db import migrations, models
import django.utils.timezone
import django_countries.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('slug', models.SlugField(blank=True, default='', null=True, verbose_name='Slug')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email')),
                ('username', models.CharField(max_length=255, unique=True, verbose_name='Username/Alias')),
                ('other_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Other name')),
                ('dob', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('website', models.URLField(blank=True, max_length=255, null=True, verbose_name='My website')),
                ('phone_1', models.CharField(blank=True, max_length=255, null=True, verbose_name='Phone number')),
                ('phone_2', models.CharField(blank=True, max_length=255, null=True, verbose_name='Extra Phone number')),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('state', models.CharField(blank=True, max_length=255, null=True, verbose_name='State')),
                ('postal', models.CharField(blank=True, max_length=255, null=True, verbose_name='ZIP/Postal code')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Select Gender', max_length=50, verbose_name='Gender')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
    ]
