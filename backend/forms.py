from django import forms
from django.utils.safestring import mark_safe

import datetime

from backend.models import File


class TextWidget(forms.Widget):
    def render(self, name, value, attrs=None, renderer=None):
        return mark_safe(value) if value is not None else '-'


class UploadFileForm(forms.ModelForm):
    '''
    Upload File Form
    '''
    period = forms.ChoiceField(choices=[
        ('hour', '1 Hour'), ('day', '1 Day'),
        ('week', '1 Week'), ('month', '1 Month'),
    ], label="Expiry")

    def __init__(self, *args, **kwargs):
        # https://stackoverflow.com/a/28653899
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if not self.user:
            # https://stackoverflow.com/a/23912332
            del self.fields['is_private'].widget.choices[1]

    def save(self, commit=True):
        m = super().save(commit=False)
        m.owner = self.user

        value = self.data['period']
        date = datetime.datetime.now()
        if value == 'hour':
            date += datetime.timedelta(hours=1)
        elif value == 'day':
            date += datetime.timedelta(days=1)
        elif value == 'week':
            date += datetime.timedelta(weeks=1)
        else:
            date += datetime.timedelta(days=30)
        m.expiry = date

        if commit:
            m.save()
        return m

    class Meta:
        model = File
        fields = ('url', 'description', 'upload', 'is_private')
        widgets = {
            'is_private': forms.RadioSelect(choices=[
                (False, 'Public'), (True, 'Private'),
            ]),
        }
        labels = {
            "url": "Custom URL",
            "description": "Description",
            "upload": "File",
            "is_private": "Visibility",
        }


class UpdateFileForm(forms.ModelForm):
    '''
    Re-Upload File Form
    '''
    class Meta:
        model = File
        fields = ('upload',)

    def save(self, commit=True, prev_file=None):
        m = super().save(commit=False)
        m.prev_file = prev_file
        if commit:
            m.save()
        if prev_file:
            prev_file.next_file = m
            prev_file.save()
        return m


class ShowFileForm(forms.Form):
    '''
    Show File Form
    '''
    url = forms.CharField(
        widget=TextWidget,
        label="Shareable URL",
    )
    description = forms.CharField(
        widget=TextWidget,
        label="Description",
    )
    is_private = forms.CharField(
        widget=TextWidget,
        label="Visibility",
    )
    expiry = forms.CharField(
        widget=TextWidget,
        label="Expiry",
    )

