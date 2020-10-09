from django.conf import settings
from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator

import os

from cloudinary_storage.storage import RawMediaCloudinaryStorage

# Create your models here.

AlphaNumericValidator = RegexValidator(r'^[0-9a-zA-Z]*$',
    'Only alphanumeric characters are allowed.'
)

class File(models.Model):
    '''
    File Object
    '''
    url = models.CharField(
        max_length=10,
        primary_key=True,
        validators=[AlphaNumericValidator],
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    is_private = models.BooleanField(default=False)
    expiry = models.DateTimeField()
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    upload = models.FileField(
        upload_to='',
        storage=RawMediaCloudinaryStorage(),
    )
    content_type = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    prev_file = models.ForeignKey(
        'File',
        related_name="prev_version",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    next_file = models.ForeignKey(
        'File',
        related_name="next_version",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        # https://stackoverflow.com/a/51928367
        if not self.content_type:
            self.content_type = self.upload.file.content_type
        if not self.name:
            self.name = self.upload.file.name
        super().save(args, kwargs)

    def get_absolute_url(self):
        return reverse('show', kwargs={'file_url': self.url})

    def __str__(self):
        return self.url + ": " + self.upload.name

