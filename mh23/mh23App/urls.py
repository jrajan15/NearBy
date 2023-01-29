from django.urls import path, include
from . import views
from .views import home
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from .views import UserView, signup


urlpatterns = [
    path('', views.home, name='home'),
    path('notifications', views.notifications, name='notifications'),
    path('events', views.events, name='events'),
    path('messages', views.messages, name='messages'),
    path('settings', views.settings, name='settings'),
	path('filter_data', views.filter_data, name='filter_data'),
	path('image_upload',views. post_image_view, name='image_upload'),
    path('success', views.success, name='success'),
	# path('', views.index, name='home')
	# path('login', views.login_page, name='login'),
    # path('logout', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    # path('accounts/profile/', login_required(views.UserView.as_view()), name='profile'),
    # path('signup', views.signup, name='signup')

]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
