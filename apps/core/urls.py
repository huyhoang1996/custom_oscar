from django.conf.urls import include, url
import views


urlpatterns = [
	url(r'^plan/$', views.PlanListView.as_view(), name='plan'),
	url(r'^plan/create/$', views.PlanCreateView.as_view(), name='plan-create'),
	url(r'^plan/update/(?P<pk>[0-9]+)/$', views.PlanUpdateView.as_view(), name='plan-update'),

    
]