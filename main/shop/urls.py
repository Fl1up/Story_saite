from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from main.shop.apps import ShopConfig
from main.shop.views import main, contact, ShopListView

app_name = ShopConfig.name

urlpatterns = [
                  path("", main, name="main"),

                  path("contact/", contact, name="contact"),

                  path("shop/", ShopListView.as_view(), name="list"),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
