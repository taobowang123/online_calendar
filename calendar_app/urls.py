from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome),
    path('createaccount/', views.create_account,name='create_account'),
    path('welcome/', views.welcome, name='welcome'),
    path('addEvents/', views.addEvents,name='addEvents'),
    path('deleteEvents/', views.deleteEvents,name='deleteEvents'),
    path('editEvents/', views.editEvents,name='editEvents'),
    path('searchEvents/', views.searchEvents,name='searchEvents'),
    path('shareEvents/', views.shareEvents,name='shareEvents'),
    path('settingsInfo/', views.settingsInfo,name='settingsInfo'),
    path('accounts/logout/', views.logout_view,name='logout'),
    path('accounts/login/', views.index,name='login'),

]
