from django.urls import path
from .views import CartView

urlpatterns =[
    path("", CartView.as_view()),
    path("<int:id>/update", CartView.as_view()),
    path("<int:id>/delete", CartView.as_view())
]