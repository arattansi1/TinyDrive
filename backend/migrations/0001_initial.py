# Generated by Django 2.1.7 on 2019-03-31 22:46

import cloudinary_storage.storage
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('url', models.CharField(max_length=10, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')])),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('is_private', models.BooleanField(default=False)),
                ('expiry', models.DateTimeField()),
                ('upload', models.FileField(storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(), upload_to='')),
                ('content_type', models.CharField(blank=True, max_length=255, null=True)),
                ('next_file', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next_version', to='backend.File')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('prev_file', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='prev_version', to='backend.File')),
            ],
        ),
    ]
