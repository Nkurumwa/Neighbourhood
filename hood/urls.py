from django.urls import url
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('', views.index, name='index'),
    url('create/profile/',views.create_profile, name='create-profile'),
    url('home/', views.home, name='home'),
    url('add/hood/', views.add_hood, name='add_hood'),
    url('join_hood/<int:hood_id>', views.join_hood, name='join_hood'),
    url('leave_hood/<int:hood_id>', views.leave_hood, name='leave_hood'),
    url('add/business/', views.add_business, name='add_business'),
    url('add/post/', views.add_post, name='add_post'),
    url('user/<username>', views.user_profile, name='user_profile'),
    url('search_results/', views.search_results, name='search_results'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)