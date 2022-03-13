
from argparse import Namespace
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
import account
from account.views import home_page

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', home_page, name='home'),
    path('account/', include('account.urls', namespace='user')),
    path('post/', include('feed.urls', namespace='post')),
    path('users/', include('users.urls', namespace='users')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
