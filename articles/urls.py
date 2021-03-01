from django.urls import path
from . import views  # from . import from the same directory you're in

urlpatterns = [
    path('', views.article_list),  # homepages have their url path set as an empty string
]