from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = "posts"

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)