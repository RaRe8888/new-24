from django.urls import path
from .views import UserRegistrationView

app_name = "accounts"
urlpatterns = [
    path("sign-up", UserRegistrationView.as_view(),name="signup")
]