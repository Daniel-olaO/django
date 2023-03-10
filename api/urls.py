from django.urls import path
from .views import RegisterView, LoginView, UserView, LogoutView, SubscriptionView, RouteListView

urlpatterns = [
    path('', RouteListView.as_view()), 
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
    path('toggle-subscription/<int:id>/', SubscriptionView.as_view()),
]
