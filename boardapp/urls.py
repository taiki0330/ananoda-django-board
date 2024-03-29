from django.urls import path
from .views import signupfunc, loginfunc, listfunc, logoutfunc
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('list/', listfunc, name='list'),
    path('logout/', logoutfunc, name='logout')
]+  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
