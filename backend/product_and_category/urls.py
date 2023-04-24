from django.urls import path
from .views import ProductView
from .views import CategoryView
urlpatterns = [
    path("product/", ProductView.as_view()),
    path("product/<int:id>/update", ProductView.as_view()),
    path("product/<int:id>/delete", ProductView.as_view()),
    path("category/", CategoryView.as_view()),
    path("category/<int:id>/update", CategoryView.as_view()),
    path("category/<int:id>/delete", CategoryView.as_view()),
]

