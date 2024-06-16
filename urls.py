
from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index',views.home,name="index"),
    path('gallery',views.gallery,name="gallery"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('home',views.home,name="home"),
  
 
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
