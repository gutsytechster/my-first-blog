from django.urls import path, re_path
from . import views

urlpatterns = [
	path('', views.post_list, name='post_list'),
	path('post/<int:kp>/', views.post_detail, name='post_detail'),
	# re_path(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]