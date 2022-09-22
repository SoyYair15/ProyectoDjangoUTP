from django.urls import path
from . import views

app_name = 'main'

urlpatterns= [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('', views.IndexView.as_view(), name='home'),
    path('blog/', views.BlogView.as_view(), name='blogs'),
    path('blog/<slug:slug>', views.BlogDetailView.as_view(), name='blog'),
    path('review/', views.ReviewView.as_view(), name='reviews'),
    path('review/<slug:slug>', views.ReviewDetailView.as_view(), name='review'),
    path('blogaddinfo/', views.BlogAddInfo.as_view(), name='blogaddinfo'),
    path('reviewaddinfo/', views.ReviewAddInfo.as_view(), name='reviewaddinfo'),
    
]

#APARTADO PARA USAR LOS URLS CREADOS A TRAVÉS DE UN NOMBRE Y QUE TE REDIRIGA AL ENLACE SELECCIONADO Y ANTERIORMENTE CREADO, EN ESTE CASO LOS DE LOS HTML