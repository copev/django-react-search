from django.urls import include, path, re_path
from . import views

from .views import OrgListDetailFilter
from rest_framework.routers import DefaultRouter
from django.urls import path

app_name = 'myapi'

router = DefaultRouter()
router.register(r'organizations', views.OrganizationViewSet),

urlpatterns = [
    path('', include(router.urls)),
    path('orgsearch/', OrgListDetailFilter.as_view(), name='orgssearch'),
]
