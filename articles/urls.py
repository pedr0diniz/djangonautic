from django.urls import path
from . import views  # from . import from the same directory you're in

app_name = 'articles'

urlpatterns = [
    path('', views.article_list, name="list"),  # homepages have their url path set as an empty string
    path('<slug:slug>/', views.article_detail, name="detail")   # first slug: parameter name
                                                                # second slug: name of the variable passed along the method
]