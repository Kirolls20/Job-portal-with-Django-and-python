from django.contrib import admin
from django.urls import path,include
from django.conf import settings 
from django.conf.urls.static import static


urlpatterns = [
    path('jet/',include('jet.urls','jet')),
    path('admin/', admin.site.urls),
    path('jet/dashboard/',include('jet.dashboard.urls','jet-dashboard')),
    path('',include('main.urls')),
    path('accounts/',include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL,document_root=settings.MEDIA_ROOT)
    