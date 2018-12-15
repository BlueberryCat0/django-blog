from django.urls import path

from .views import ProfileDetailView

app_name = 'accounts'

urlpatterns = [
    path('profile/<int:id>/', ProfileDetailView.as_view(), name='profile_details'),
]
