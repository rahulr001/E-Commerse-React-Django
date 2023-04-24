from django.urls import path
from .views import OrderView

urlpatterns = [
    path("", OrderView.as_view()),
    path("<int:id>/update", OrderView.as_view()),
    path("<int:id>/delete", OrderView.as_view()),

]
