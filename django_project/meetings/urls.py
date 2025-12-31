from django.urls import path
from .views.user_views import user_views
from .views.meeting_views import meeting_views,updatemeeting,serach
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('users/', user_views),  # GET/POST sur /users/
    path('token/' , TokenObtainPairView.as_view() ) ,
    path ('token/refresh/' ,TokenRefreshView.as_view() ),
    path ('meeting/' ,meeting_views),
    path ('updatemeeting/' ,updatemeeting),
    path ('search/',serach)




]
