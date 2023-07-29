
from django.contrib import admin
from django.urls import path,include
from app1.views import *

from drf_spectacular.views import SpectacularAPIView, \
    SpectacularRedocView, \
    SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apiview_docs/', SpectacularAPIView.as_view(), name="schema"),
    path('docs/', SpectacularSwaggerView.as_view(url_name = "schema")),
    path('tolovlar/', TolovlarAPIView.as_view()),
    path('oquvchilar/', OquvchilarAPIView.as_view()),
    path('davomatlar/', DavomatlarAPIView.as_view()),
]
