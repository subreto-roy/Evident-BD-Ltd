
from django.contrib import admin
from django.urls import path
from user_auth import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('logout/',views.LogoutPage,name='logout'),
    path('khuj/',views.khoj_search,name='khoj_search'),
    path('api/',views.input_history_api, name='input_history_api'),

]

