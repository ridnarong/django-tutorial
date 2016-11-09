from django.conf.urls import include, url
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'messages', views.MessageViewSet)

urlpatterns = [
	url(r'^', include(router.urls)),
	url(r'^hi/$', views.HomeView.hi)
]