from django.urls import path
from .views import login_view, logout_view, update_user, profile, register_view, confirm_your_email, \
    register_activate_email
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path("update/", update_user, name="update"),
    path("profile/<str:username>/", profile, name="profile"),
    path('sign-up', register_view, name='register'),
    path('sign-in', login_view, name='login'),
    path('confirm-your-email',confirm_your_email, name='confirm_your_email'),
    path('activate-register/<str:uid>/<str:token>', register_activate_email),
    path('logout/', logout_view, name='logout')

]
