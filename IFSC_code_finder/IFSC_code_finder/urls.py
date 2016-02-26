"""IFSC_code_finder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import(
    landing_page,
    serve_bank_names,
    send_branch_ifsc_code
    )

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',landing_page),
    url(r'^serve_bank_names/$',serve_bank_names),
    url(r'^get_branch_ifsc_code/$',send_branch_ifsc_code),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
