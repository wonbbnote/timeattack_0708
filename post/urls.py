from django.contrib import admin
from django.urls import path, include
from .views import SkillView, JobView
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    path('', SkillView.as_view()),

    path('job', JobView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
]
