from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('activities/', include('activities.urls')),
    path('blog/', include('blog.urls')),
    path('finance/', include('finance.urls')),
    path('devotionals/', include('devotionals.urls')),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
