from django.contrib import admin
from django.urls import path
from appnew import views

# from applogin import views
app_name = 'appnew'
urlpatterns = [

    path('register/', views.register, name='register'),
    path('user_login/',views.user_login,name='user_login'),
    #path('product_management/',views.product_management,name='product_management'),
    path('emp/', views.emp,name='emp'),
    path('show/',views.show,name='show'),
    path('edit/<int:id>', views.edit,name='edit'),
    path('update/<int:id>', views.update,name='update'),
    path('delete/<int:id>', views.destroy,name='destroy'),


]
