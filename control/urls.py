from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'womenserver.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^index',views.index,name = 'index'),
	
	url(r'signup/',views.signup,name = 'signup'),
	url(r'login/',views.LOGIN,name = 'LOGIN'),
	url(r'savedata/',views.save_data,name = 'save_data'),
]