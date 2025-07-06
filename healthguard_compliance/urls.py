from django.urls import path, include
from rest_framework import routers
from .views import ComplianceRequirementViewSet, DocumentViewSet, NotificationViewSet
from .auth_views import RegisterView, LoginView

router = routers.DefaultRouter()
router.register(r'compliance', ComplianceRequirementViewSet, basename='compliance')
router.register(r'documents', DocumentViewSet, basename='documents')
router.register(r'notifications', NotificationViewSet, basename='notifications')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]
urlpatterns += router.urls
