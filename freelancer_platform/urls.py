
from django.contrib import admin
from django.urls import path, include
from services.views import service_list
from django.contrib.auth.views import LogoutView
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", service_list, name="home"),
    path("users/", include("users.urls")),
    path("services/", include("services.urls")),
    path("orders/", include("orders.urls")),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("orders/", include(("orders.urls", "orders"), namespace="orders")),
    path("notifications/", include("notifications.urls")),

] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)