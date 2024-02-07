"""
URL configuration for cabbook project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from cabdrivers import views as cabdrive
from django.conf import settings
from django.conf.urls.static import static

app_name = 'cabdrivers'
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', cabdrive.cabdrive_login, name='cabdrive_login'),
    path('driver_signup', cabdrive.driver_signup, name='driver_signup')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
