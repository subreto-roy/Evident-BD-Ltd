
from django.contrib import admin
from django.urls import path
from user_auth import views
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('logout/',views.LogoutPage,name='logout'),
    path('khuj/',views.khoj_search,name='khoj_search'),
    path('api/',views.input_history_api, name='input_history_api'),
    path('seasion_history_api/',views.seasion_history_api, name='seasion_history_api'),
    path('api-token-auth/', ObtainAuthToken.as_view(), name='api_token_auth'),
    

]

