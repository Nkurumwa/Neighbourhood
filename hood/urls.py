from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('create/profile/',views.create_profile, name='create-profile'),
    path('home/', views.home, name='home'),
    path('add/hood/', views.add_hood, name='add_hood'),
    path('join_hood/<int:hood_id>', views.join_hood, name='join_hood'),
    path('leave_hood/<int:hood_id>', views.leave_hood, name='leave_hood'),
    path('add/business/', views.add_business, name='add_business'),
    path('add/post/', views.add_post, name='add_post'),
    path('user/<username>', views.user_profile, name='user_profile'),
    path('search_results/', views.search_results, name='search_results'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)