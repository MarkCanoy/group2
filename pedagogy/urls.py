from django.contrib import admin
from django.urls import path

from .views import home_page, contact_page, register_page, login_page
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home_page),
    path('login/', login_page),
    path('logout/', auth_views.LogoutView.as_view(template_name="auth/logout.html"), name="logout.html"),
    path('register/', register_page),
    path('contact/', contact_page),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
