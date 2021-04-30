from django.urls import path, include

from contact import views

urlpatterns = [
    path('Home/', views.contactHome, name='home'),
    path('', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('Home/add_contact', views.addContact, name='add_contact'),
    path('Home/view_contact', views.viewContact, name='view_contact'),
    path('Home/remove_contact', views.removeContact, name='remove_contact'),
]
