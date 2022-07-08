from rest_framework.permissions import BasePermission
from datetime import timedelta
from django.utils import timezone

from user.models import User

class IsCandidateUser(BasePermission):
    """
    유저타입이 “candidate”일 때만 인가
    """
    
    def has_permission(self, request, view):
        user = User.objects.get(user=request.user)
        if user.user_type == "candidate":
            return True