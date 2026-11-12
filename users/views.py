from rest_framework.response import Response
from rest_framework.views import APIView

from .permissions import IsAdminOnly, IsUserOnly


class AdminPanelAPIView(APIView):
    permission_classes = [IsAdminOnly]

    def get(self, request):
        return Response({"message": "Добро пожаловать в панель администратора!"})


class UserDashboardAPIView(APIView):
    permission_classes = [IsUserOnly]

    def get(self, request):
        return Response({"message": "Личный кабинет пользователя"})
