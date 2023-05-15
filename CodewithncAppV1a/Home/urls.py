from django.urls import path
from .views import *
from .views_api import *

urlpatterns = [
    path('', home, name='home'),

    path('about/', about, name='about'),
    
    path('contact/', contact, name='contact'),
    
    path('courses/', courses, name='courses'),

    path('blog-single/<slug>', blogSingle, name='blogSingle'),

    path('login/', Ulogin, name='Ulogin'),

    path('signup/', signup, name='signup'),

    path('register/', registerAd, name='registerAd'),

    path('access/', accessAd, name='accessAd'),

    path('inaccess/', LogoutView, name='AccessoutView'),

    path('blog/', blog, name='blog'),

    path('recent/', recent, name='recent'),

    path('admin/', admin, name='admin'),
    
    path('courses/', courses, name='courses'),

    path('course-single/<slug>', courseSingle, name='courseSingle'),

    path('varify/<token>', varifyAd, name='varifyAd'),
]