
from django.contrib import admin
from django.urls import path
from user_auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('home/',views.HomePage,name='home'),
    path('logout/',views.LogoutPage,name='logout'),
    path('khuj/',views.khoj_search,name='khoj_search'),
    path('post_input_numbers/', views.post_input_numbers, name='get_input_values'),

]
