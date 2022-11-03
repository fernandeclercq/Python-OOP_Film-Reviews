from django.contrib import admin
from django.urls import path

from django.urls import include

from film import views as filmViews

# Used to show media on pages
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', filmViews.home, name='home'),
    path('over/', filmViews.over, name='over'),
    path('film/', include('film.urls')),
    path('nieuws/', include('nieuws.urls')),
    path('accounts/', include('accounts.urls'))
]

# Used to show media on pages
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)