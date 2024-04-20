from django.contrib import admin
from django.urls import path,include
# from News import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("News.urls")),
]
