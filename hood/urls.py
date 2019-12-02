from django.conf.urls import url
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$', views.index, name='index'),
    url(r'^create/profile/$',views.create_profile, name='create-profile'),
    url(r'^home/$', views.home, name='home'),
    url(r'^add/hood/$', views.add_hood, name='add_hood'),
    url(r'^join_hood/<int:hood_id>$', views.join_hood, name='join_hood'),
    url(r'^leave_hood/<int:hood_id>$', views.leave_hood, name='leave_hood'),
    url(r'^add/business/$', views.add_business, name='add_business'),
    url(r'^add/post/$', views.add_post, name='add_post'),
    url(r'^user/<username>$', views.user_profile, name='user_profile'),
    url(r'^search_results/$', views.search_results, name='search_results'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)