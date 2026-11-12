from django.urls import path

from .views import AdminPanelAPIView, UserDashboardAPIView


urlpatterns = [
    path("admin-panel/", AdminPanelAPIView.as_view(), name="admin-panel"),
    path("user-dashboard/", UserDashboardAPIView.as_view(), name="user-dashboard"),
]
