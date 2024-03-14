from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
     path('',views.home,name='home'),
     path('about',views.about,name='about'),
     path('contact',views.contact,name='contact'),
     path('signup',views.sign_up, name='signup'),
     path('login/',views.user_login, name='login'),
     path('logout/',views.user_logout, name='logout'),
     path('allproducts/',views.allproducts, name='allproducts'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)