from django.urls import path

from .views import HomeView, UserView

urlpatterns = [
    path("users/", UserView.as_view()),
    path("", HomeView.as_view()),
]
