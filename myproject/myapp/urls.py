from django.urls import path
from .views import FirstUserView, AllUsersView, UserProfileView

urlpatterns = [
    path('first-user/', FirstUserView.as_view(), name='first-user'),
    path('all-users/', AllUsersView.as_view(), name='all-users'),
    path('user-profile/<int:user_id>/', UserProfileView.as_view(), name='user-profile'),
]
