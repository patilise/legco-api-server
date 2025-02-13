"""api_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from api_server.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^legco/', include('legco.urls')),
    url(r'^budget/', include('budget.urls')),
    url(r'^news/', include('news.urls')),
    url(r'^gov/', include('gov.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^status/', StatusView.as_view(), name='status'),
    url(r'^party/', PartyView.as_view(), name='party'),
    url(r'^individual/', IndividualView.as_view(), name='individual'),
    url(r'^\.well-known/', include('letsencrypt.urls'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
