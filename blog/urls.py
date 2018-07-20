from django.urls import path, re_path
from . import views

urlpatterns = [
	path('', views.post_list, name='post_list'),
	path('post/<int:kp>/', views.post_detail, name='post_detail'),
	path('post/new/', views.post_new, name='post_new'),	
	path('post/<int:kp>/edit', views.post_edit, name='post_edit'),
	path('draft/', views.post_draft_list, name='post_draft_list'),
	path('post/<int:kp>/publish', views.post_publish, name='post_publish'),
	path('post/<int:kp>/remove', views.post_remove, name='post_remove'),
	# re_path(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]