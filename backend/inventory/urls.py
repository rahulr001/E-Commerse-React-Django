from django.urls import path
from .views import InventoryView
urlpatterns = [
    path("", InventoryView.as_view()),
    path("<int:id>/update", InventoryView.as_view()),
    path("<int:id>/delete", InventoryView.as_view()),
]
