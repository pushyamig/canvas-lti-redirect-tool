from django.urls import path
from . import views
from lti_tool.views import jwks, OIDCLoginInitView
urlpatterns = [
     path('', views.get_home_template, name = 'home'),

     # LTI launch urls
    path(".well-known/jwks.json", jwks, name="jwks"),
    path("init/<uuid:registration_uuid>/", OIDCLoginInitView.as_view(), name="init"),
    path("ltilaunch", views.ApplicationLaunchView.as_view(), name="ltilaunch"),
]