
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path("",include("home.urls")),
    path("testimonial/",include("testimonial.urls")),
    path("menu/",include("menu.urls")),
    path("contact/",include("contact.urls")),
    path("booking/",include("booking.urls")),
    path("about/",include("about.urls")),
    path("chef/",include("chef.urls")),
    path("blog/",include("blog.urls")),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
