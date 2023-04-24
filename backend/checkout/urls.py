from django.urls import path
from .views import CheckoutView

urlpatterns = [
    path("",CheckoutView.as_view()),
    path("<int:id>/update", CheckoutView.as_view()),
    path("<int:id>/delete", CheckoutView.as_view()),
]