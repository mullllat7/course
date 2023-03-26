# Generated by Django 4.1.6 on 2023-02-02 15:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('surname', models.CharField(blank=True, max_length=100)),
                ('money', models.FloatField(null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InfoUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='media/user_image')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='info_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Info user',
                'verbose_name_plural': 'Info users',
            },
        ),
    ]