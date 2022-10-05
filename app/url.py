from django.contrib import admin
from django.urls import path
from app.views import contact_list_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", contact_list_view, name="contact_list")
]