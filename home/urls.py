from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('natijalar/',views.natijalar,name='natijalar'),
    path('hodim/',views.hodim,name='hodim'),
    path('open/',views.open,name='open'),
    path('hodim/open/',views.open,name='open'),
    path('about/open/',views.open,name='open'),
    path('hodim/404/',views.handler404,name='handler'),
    path('open/404/',views.handler404,name='handler'),
    path('404/',views.handler404,name='handler'),
    path('about/',views.about,name='about')
]