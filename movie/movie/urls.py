"""movie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls'))
]
# urlpatterns += [path(r'^media/(?P<path>.*)$', serve,
#                     {'document_root': settings.MEDIA_ROOT, }),
#                 path(r'', include('django.contrib.staticfiles.urls')),]
# # urlpatterns += static(settings.MEDIA_URL)


from django.conf import settings
from django.conf.urls import include, url

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      url(r'^__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns


urlpatterns +=staticfiles_urlpatterns()

urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)