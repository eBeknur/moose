from django.urls import path
from . import views
from .views import category

urlpatterns = [
    path("", views.home),
    path("about/", views.about),
    path("contact/", views.contact),
    path("blog/", views.blog),
    path("blog-single/<int:pk>/",views.blog_single),
    path("category/<str:pk>/" , views.category),
]
