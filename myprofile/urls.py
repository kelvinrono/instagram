from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns=[
    url('^$',views.home,name='home'),
    url(r'accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url('profile/<str:username>/',views.profile,name='profile'),
    url('edit/profile/',views.update_profile,name='update'),
    url('user_profile/<username>/', views.user_profile, name='user_profile'),


]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)