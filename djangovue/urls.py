"""tinydrive URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import include, path
from django.conf import settings

from backend import views

urlpatterns = [
    # Auth0
    path('login', views.login),
    path('', include('django.contrib.auth.urls')),
    path('', include('social_django.urls')),

    # Files
    path('', views.index, name='index'),
    path('upload', views.UploadFileView.as_view(), name='upload'),
    path('update/<file_url>', views.update, name='update'),
    path('show/<file_url>', views.show, name='show'),
    path('download/<file_url>', views.download, name='download'),
    path('delete/<file_url>', views.delete, name='delete'),

    # Templates
    path('credits', views.credits, name='credits'),
]

handler400 = views.handler400
handler403 = views.handler403
handler404 = views.handler404
handler500 = views.handler500
