from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'polls', views.QuestionViewSet)
router.register(r'choice', views.ChoiceViewSet)

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="home.html")),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^api/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
]

