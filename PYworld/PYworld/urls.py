from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('productos/', include('PYworld_Apps.urls')),
    path('admin/', admin.site.urls),
]