from django.urls import path
from . import views

urlpatterns = [
   # path('admin/', admin.site.urls),
    path('teacher',views.hello_world,name='hello_world'),
    path('home',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('profile',views.profile,name='profile'),
    path('courses',views.courses,name='courses'),
]