from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied, SuspiciousOperation
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required

import json
import random
import string
import time

from backend.forms import UploadFileForm, ShowFileForm, UpdateFileForm
from backend.models import File


# Create your views here.

def handler400(request, exception):
    return render(request, '400.html', status=400)


def handler403(request, exception):
    return render(request, '403.html', status=403)


def handler404(request, exception):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)


def get_file(user, url):
    '''
    Helper function to retrieve File object from database,
    with permission checks.
    '''
    file = get_object_or_404(File, pk=url)
    if file.is_private and user != file.owner:
        raise PermissionDenied
    return file


def generate_id():
    while True:
        id = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        if not File.objects.filter(pk=id).exists():
            return id


def login(request):
    return render(request, 'login.html')


def credits(request):
    return render(request, 'credits.html', {
        'is_anonymous': request.user.is_anonymous,
    })


def index(request):
    return render(request, 'index.html', {
        'is_anonymous': request.user.is_anonymous,
    })


def download(request, file_url):
    # https://stackoverflow.com/a/9463976
    file = get_file(request.user, file_url)
    response = HttpResponse(file.upload, content_type=file.content_type)
    response['Content-Disposition'] = 'attachment; filename=%s' % file.name
    return response


def show(request, file_url):
    file = get_file(request.user, file_url)
    show_form = ShowFileForm(initial={
        'url': '<a href="' + file.get_absolute_url()
            + '">' + request.build_absolute_uri() +'</a>',
        'description': file.description,
        'is_private': 'Private' if file.is_private else 'Public',
        'expiry': file.expiry.strftime("%m/%d/%Y, %H:%M:%S") + " UTC",
    })
    update_form = UpdateFileForm()

    # file show
    return render(request, 'show.html', {
        'file': file,
        'show_form': show_form,
        'update_form': update_form,
        'is_anonymous': request.user.is_anonymous,
        'allow_edit': not (file.owner and file.owner != request.user),
    })


def update(request, file_url):
    '''
    Generate new URL for original file
    Upload new file the original url
    '''
    if request.method == 'POST':
        old_file = get_file(request.user, file_url)
        if old_file.owner and old_file.owner != request.user:
            raise PermissionDenied
        if old_file.next_file:
            raise SuspiciousOperation

        old_file.pk = generate_id()
        new_file = get_file(request.user, file_url)
        form = UpdateFileForm(request.POST, request.FILES, instance=new_file)

        if form.is_valid():
            old_file.save()
            form.save(prev_file=old_file)
            return redirect(new_file)

    return redirect('index')


def delete(request, file_url):
    file = get_file(request.user, file_url)
    if file.owner and file.owner != request.user:
        raise PermissionDenied
    file.delete()
    return redirect('index')


class UploadFileView(CreateView):
    form_class = UploadFileForm
    template_name = 'upload.html'

    def get_form_kwargs(self):
        # https://stackoverflow.com/a/28669154
        kwargs = super().get_form_kwargs()
        if not self.request.user.is_anonymous:
            kwargs.update(user=self.request.user)
        return kwargs

    def get_context_data(self, **kwargs):
        kwargs['is_anonymous'] = self.request.user.is_anonymous
        return super().get_context_data(**kwargs)
